#!/usr/bin/env python3
"""fsla-results's front door stub: bazelisk runs `bazel/bazel` (this file, the wrapper `.bazeliskrc` names) in place of the
Bazel it downloaded, and it runs fsla-devtools' front door (`fsla_devtools.graph.front_door`) for this checkout, from
the machine's fsla-devtools checkout -- `workspace.devtools` in the dev config's workspace section, else the sibling
`fsla-devtools` beside this checkout (a worktree's beside its worktrees folder). `--tripwire ARGS` runs fsla_devtools.tripwire (the hooks'). Standard library only: it runs before
any environment exists."""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

sys.dont_write_bytecode = True  # the front door runs from the checkout: it leaves no bytecode there
ROOT = Path(__file__).resolve().parents[1]
SIBLINGS = (ROOT.parent if ROOT.parent.name == "worktrees" else ROOT).parent


def devtools() -> Path:
    pointer = os.environ.get("FSLA_DEV_CONFIG")
    section = (Path(pointer).expanduser() if pointer else Path.home() / ".config" / "fsla") / "workspace.json"
    value = json.loads(section.read_text()).get("devtools") if section.is_file() else None
    return Path(value).expanduser() if value else SIBLINGS / "fsla-devtools"


sys.path.insert(0, str(devtools()))
from fsla_devtools.graph import front_door  # noqa: E402 -- the path insert above must precede it

if __name__ == "__main__":
    if sys.argv[1:2] == ["--tripwire"]:  # the hooks' content checks (fsla_devtools.tripwire), from the same checkout
        from fsla_devtools import tripwire  # noqa: E402

        sys.exit(tripwire.main(sys.argv[2:]))
    sys.exit(front_door.main(sys.argv[1:], ROOT))
