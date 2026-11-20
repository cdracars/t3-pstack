"""Append one evidence-linked decision row without shell interpolation."""

import argparse
import csv
from datetime import datetime, timezone
from pathlib import Path

HEADER = ["ts", "phase", "decision", "why", "evidence", "result"]


def cell(value):
    value = value.replace("\t", " ").replace("\r", " ").replace("\n", " ")
    return "'" + value if value.lstrip().startswith(("=", "+", "-", "@")) else value


def append(path, values):
    path = Path(path)
    if path.exists() and path.stat().st_size:
        with path.open(encoding="utf-8", newline="") as source:
            if next(csv.reader(source, delimiter="\t"), None) != HEADER:
                raise ValueError("Existing log has a different header; choose its own writer or a new log")
        with path.open("rb") as source:
            source.seek(-1, 2)
            if source.read(1) != b"\n":
                raise ValueError("Existing log ends in a partial row; preserve it and reconcile before appending")
    path.parent.mkdir(parents=True, exist_ok=True)
    needs_header = not path.exists() or path.stat().st_size == 0
    with path.open("a", encoding="utf-8", newline="") as output:
        writer = csv.writer(output, delimiter="\t", lineterminator="\n")
        if needs_header:
            writer.writerow(HEADER)
        stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
        writer.writerow([stamp, *(cell(value) for value in values)])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("log", type=Path)
    for name in HEADER[1:]:
        parser.add_argument(name)
    args = parser.parse_args()
    try:
        append(args.log, [getattr(args, name) for name in HEADER[1:]])
    except (ValueError, OSError) as error:
        parser.exit(1, f"decision log: {error}\n")
