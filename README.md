# fsla-results

The measurement records every reported FSLA number is read from: a repository of data and no code. The store's code --
writing a record, checking them, the index and its views, the verdict, the dashboard -- is fsla-devtools'
(`fsla_devtools.results`); this repository holds what it stored.

    records/<location>/<key>.json            a record (format 1: key, location, format, semantics, samples)
    records/<location>/<key>.<n>.out.<ext>   sample n's output
    lab/<experiment>/...                     the lab's records (fsla's `measure/lab/results/`, moved here with their
                                             history, byte-identical), kept as written

- **A location** names who stores: `fsla/sass`, `timing/session`, `mqar/<config>`, `environment`.
- **A record** is everything kept under one key: the semantics the tool handed over and every sample.
- **The key** is sha256 over the semantics, so a repeat lands on the same record and a changed input on a new one.
- **A sample** is one execution: its output or its error, when, how long, its provenance (the checkouts and commits
  the tool names; the host).

Nothing derived from two records (a ratio, a baseline) is stored: that is the reader's. A recorded result is never
rewritten; a new run is a new sample. fsla-devtools' README (`The results store`) is the store's whole contract: what a
record holds, the refusals at the door (a machine path, a timing without its commits), the index's tables and views,
and the verdict.

## Who writes here and who reads it

A tool writes a record through `fsla_devtools.results.Store`, at the checkout the machine's dev config names as
`store.root`, its `records/` the backend. A measurement taken on a rented card comes back as a patch, applied here,
checked by this repository's gate, committed and pushed from the desk -- a rented box never holds push credentials.
fsla pins this repository at ONE commit (fsla-devtools' `environment.data` tag, by the commit's archive digest) and
cites a record by its path inside it (`data:lab/reg_trade/sm_90a.json`, `data:records/...`), so a citation resolves to
fixed content; moving the pin to a newer commit is how a new record becomes citable.

## The gate and the index

    bazel test //:gate        every record consistent, every lab file parsed, every path declared
    bazel build //:index      the records' SQLite index and views: a build output, never a file beside the records

The gate is the store's own check over `records/` (`python3 -m fsla_devtools.results --root records check`: every key
recomputes from its semantics, every location is its directory, every successful sample's output exists), the same over
`lab/` (`check-files lab`: each file parses where it is JSON or CSV), and the declaration
check (`python -m fsla_devtools.mirror --check`). Its environment is the standard library and fsla_devtools, from the
module's source at the pinned commit (the front door overrides it with the machine's fsla-devtools checkout). The
commit hook (`.githooks/pre-commit` -> `bazel/bazel --commit-gate`, fsla-devtools' commit gate) runs it on the commit as
git will write it.

The store's command line runs on this checkout's records by `--root`:

    bazel run //:results -- --root records show [LOCATION]
    bazel run //:results -- --root records sql "SELECT ..."
    bazel run //:results -- --root records verdict --reference LABEL

Bazel is fsla's pinned bazelisk (a fsla checkout's `python3 tools/bootstrap.py` links it), run through this checkout's
front door (`bazel/bazel`), which runs fsla-devtools' from the machine's fsla-devtools checkout.

## Publishing

This repository is developed in public, with its whole history. A record carries no machine path -- the store refuses
one at the door (a path inside a home directory) -- so every record is stored as written.
