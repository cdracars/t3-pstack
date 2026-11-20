import csv
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("trial_builder", ROOT / "tools/trial.py")
trial = importlib.util.module_from_spec(spec)
spec.loader.exec_module(trial)


class TrialPackaging(unittest.TestCase):
    def test_installed_shape_is_self_contained_and_detects_drift(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            shutil.copytree(ROOT / "trial", target / "trial")
            for entry in json.loads((target / "trial/sources.json").read_text())["skills"]:
                source = Path(entry["source"])
                (target / source).parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / source, target / source)
            shutil.copyfile(ROOT / "LICENSE", target / "LICENSE")
            shutil.copyfile(ROOT / "plugins/pstack/LICENSE", target / "plugins/pstack/LICENSE")
            trial.build(target)
            self.assertEqual(trial.check(target), [])
            runtime = target / "trial/skills/pstack-recall/references/runtime.md"
            runtime.write_text("old adapter")
            self.assertTrue(any("pstack-recall/references/runtime.md" in error for error in trial.check(target)))


class DecisionLog(unittest.TestCase):
    def invoke(self, path, *cells):
        return subprocess.run([sys.executable, str(ROOT / "trial/log.py"), str(path), *cells], capture_output=True, text=True)

    def test_appends_real_tsv_and_escapes_formula_prefixes(self):
        with tempfile.TemporaryDirectory() as directory:
            log = Path(directory) / "nested/decisions.tsv"
            first = self.invoke(log, "start", "=SUM(1,2)", "because\nwe checked", "@artifact\tname", "verified")
            self.assertEqual(first.returncode, 0, first.stderr)
            second = self.invoke(log, "check", "observed result", "matched source", "evidence.json", "inconclusive")
            self.assertEqual(second.returncode, 0, second.stderr)
            with log.open(encoding="utf-8", newline="") as source:
                rows = list(csv.reader(source, delimiter="\t"))
            self.assertEqual(len(rows), 3)
            self.assertTrue(all(len(row) == 6 for row in rows))
            self.assertEqual(rows[1][2:5], ["'=SUM(1,2)", "because we checked", "'@artifact name"])

    def test_refuses_a_foreign_header_or_partial_row_without_mutating_it(self):
        with tempfile.TemporaryDirectory() as directory:
            log = Path(directory) / "decisions.tsv"
            for payload in [b"another\theader\n", b"ts\tphase\tdecision\twhy\tevidence\tresult\npartial"]:
                log.write_bytes(payload)
                result = self.invoke(log, "check", "choice", "reason", "proof", "open")
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(log.read_bytes(), payload)


if __name__ == "__main__":
    unittest.main()
