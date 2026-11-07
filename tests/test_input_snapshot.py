"""Mechanical snapshot checks. These do not test SAS semantics or host skill invocation."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "input_snapshot", Path(__file__).resolve().parents[1] / "scripts" / "input_snapshot.py")
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)


class SnapshotTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.input = self.root / "input"
        self.input.mkdir()
        (self.input / "source.sas.txt").write_text("data work.a; run;\n", encoding="utf-8")
        self.manifest = self.root / "manifest.json"

    def test_create_and_read_only_check(self):
        value = helper.create(self.input, self.manifest)
        original = self.manifest.read_bytes()
        self.assertEqual(value, helper.check(self.input, self.manifest))
        self.assertEqual(original, self.manifest.read_bytes())

    def test_reproducible_snapshot(self):
        self.assertEqual(helper.snapshot(self.input), helper.snapshot(self.input))

    def test_modified_source_fails_without_rewriting_manifest(self):
        helper.create(self.input, self.manifest)
        original = self.manifest.read_bytes()
        (self.input / "source.sas.txt").write_text("changed\n", encoding="utf-8")
        with self.assertRaises(ValueError):
            helper.check(self.input, self.manifest)
        self.assertEqual(original, self.manifest.read_bytes())

    def test_added_or_removed_input_fails(self):
        helper.create(self.input, self.manifest)
        other = self.input / "include.txt"
        other.write_text("new", encoding="utf-8")
        with self.assertRaises(ValueError):
            helper.check(self.input, self.manifest)
        other.unlink()
        (self.input / "source.sas.txt").unlink()
        with self.assertRaises(ValueError):
            helper.check(self.input, self.manifest)

    def test_manifest_tampering_fails(self):
        helper.create(self.input, self.manifest)
        record = json.loads(self.manifest.read_text())
        record["snapshot_sha256"] = "0" * 64
        self.manifest.write_text(json.dumps(record), encoding="utf-8")
        with self.assertRaises(ValueError):
            helper.check(self.input, self.manifest)

    def test_duplicate_manifest_key_fails(self):
        self.manifest.write_text('{"version":1,"version":1}', encoding="utf-8")
        with self.assertRaises(ValueError):
            helper.check(self.input, self.manifest)

    def test_no_manifest_overwrite(self):
        helper.create(self.input, self.manifest)
        with self.assertRaises(FileExistsError):
            helper.create(self.input, self.manifest)

    def test_manifest_inside_input_rejected(self):
        with self.assertRaises(ValueError):
            helper.create(self.input, self.input / "manifest.json")

    def test_symlink_input_rejected(self):
        link = self.input / "alias"
        try:
            link.symlink_to(self.root / "outside")
        except (OSError, NotImplementedError):
            self.skipTest("Symlinks unavailable on this host")
        with self.assertRaises(ValueError):
            helper.snapshot(self.input)

    def test_nested_file_recorded(self):
        nested = self.input / "folder"
        nested.mkdir()
        (nested / "child.txt").write_text("child", encoding="utf-8")
        paths = {item["path"] for item in helper.snapshot(self.input)["files"]}
        self.assertIn("folder/child.txt", paths)


if __name__ == "__main__":
    unittest.main()
