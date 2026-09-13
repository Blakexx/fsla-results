"""The store's contract, on a temporary backend (no GPU, no git)."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from .store import Store, check, key, locations


class StoreContract(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.store = Store("tool/sub", self.root)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_the_same_semantics_land_on_one_record_and_every_sample_is_kept(self) -> None:
        sem = {"cell": "a", "binary": "b1"}
        self.store.put(sem, output={"ms": 1.0}, provenance={"git_sha": "x"}, wall_s=0.5)
        self.store.put(sem, error="boom")
        self.store.put(sem, output={"ms": 2.0})
        record = self.store.get(key(sem))
        self.assertEqual([s["ok"] for s in record["samples"]], [True, False, True])
        self.assertEqual(record["samples"][0]["provenance"]["git_sha"], "x")
        self.assertIn("host", record["samples"][0]["provenance"])
        self.assertEqual(json.loads(self.store.output(record).read_text()), {"ms": 2.0})
        self.assertEqual(json.loads(self.store.output(record, 0).read_text()), {"ms": 1.0})
        self.assertTrue(Store.complete(record))

    def test_a_record_of_failures_is_not_complete(self) -> None:
        sem = {"cell": "b"}
        self.store.put(sem, error="first")
        record = self.store.get(key(sem))
        self.assertFalse(Store.complete(record))
        with self.assertRaises(LookupError):
            self.store.output(record)

    def test_a_changed_input_is_a_new_record(self) -> None:
        self.store.put({"binary": "b1"}, output=1)
        self.store.put({"binary": "b2"}, output=1)
        self.assertEqual(len(list(self.store.records())), 2)

    def test_an_output_file_is_moved_in_with_its_suffix(self) -> None:
        src = self.root / "capture.csv"
        src.write_text("a,b\n")
        sample = self.store.put({"cell": "c"}, output_file=src)
        self.assertEqual(sample["output"], f"{key({'cell': 'c'})}.0.out.csv")
        self.assertFalse(src.exists())

    def test_a_sample_is_exactly_one_of_output_or_error(self) -> None:
        with self.assertRaises(ValueError):
            self.store.put({"x": 1})
        with self.assertRaises(ValueError):
            self.store.put({"x": 1}, output=1, error="e")

    def test_a_location_is_a_relative_path_of_plain_names(self) -> None:
        for bad in ("", "/abs", "a/../b", "a b", "a//b"):
            with self.assertRaises(ValueError):
                Store(bad, self.root)

    def test_check_finds_a_record_whose_semantics_were_edited(self) -> None:
        self.store.put({"cell": "d"}, output=1)
        self.assertEqual(check(self.root), [])
        self.assertEqual(locations(self.root), ["tool/sub"])
        path = self.store.path(key({"cell": "d"}))
        record = json.loads(path.read_text())
        record["semantics"]["cell"] = "e"
        path.write_text(json.dumps(record))
        self.assertTrue(any("does not recompute" in p for p in check(self.root)))


if __name__ == "__main__":
    unittest.main()
