"""python -m rola_results check | show [LOCATION] | commit -m MESSAGE [--root DIR]"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from .store import ROOT, Store, check, locations


def main() -> int:
    ap = argparse.ArgumentParser(prog="python -m rola_results")
    ap.add_argument("--root", type=Path, default=ROOT, help="the backend's directory (default: this repository's records/)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check", help="every record's key recomputes, its location is its directory, its outputs exist")
    show = sub.add_parser("show", help="the locations, or one location's records")
    show.add_argument("location", nargs="?")
    commit = sub.add_parser("commit", help="commit the records (never the library) in the backend's git repository")
    commit.add_argument("-m", "--message", required=True)
    a = ap.parse_args()

    if a.cmd == "check":
        problems = check(a.root)
        print("\n".join(problems) or f"records: {sum(1 for _ in a.root.rglob('*.json'))} files under {len(locations(a.root))} "
              "locations, all consistent")
        return 1 if problems else 0

    if a.cmd == "show":
        if not a.location:
            for loc in locations(a.root):
                print(f"{loc:<40}{sum(1 for _ in Store(loc, a.root).records())} records")
            return 0
        for record in Store(a.location, a.root).records():
            ok = sum(s["ok"] for s in record["samples"])
            last = record["samples"][-1] if record["samples"] else {}
            print(f"{record['key']}  {ok} ok / {len(record['samples']) - ok} failed  last {last.get('utc', '-')}")
        return 0

    problems = check(a.root)
    if problems:
        print("\n".join(problems), file=sys.stderr)
        return 1
    repo = subprocess.run(["git", "-C", str(a.root), "rev-parse", "--show-toplevel"], capture_output=True, text=True,
                          check=True).stdout.strip()
    subprocess.run(["git", "-C", repo, "add", "--", str(a.root)], check=True)
    return subprocess.run(["git", "-C", repo, "commit", "-m", a.message, "--", str(a.root)], check=False).returncode


if __name__ == "__main__":
    sys.exit(main())
