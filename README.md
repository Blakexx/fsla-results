# fsla-results

The measurement records every reported FSLA number is read from: a repository of data and no code. The store's code --
writing a record, checking them, the index and its views, the verdict, the dashboard -- is fsla-devtools'
(`fsla_devtools.results`); this repository holds what it stored.

    records/<workspace>/<package>/<target>/<run>.json      a sample (format 2: label, key, semantics, run, provenance,
                                                           output or error)
    records/<workspace>/<package>/<target>/<run>/          its output (`output.<ext>`) and its parts (a traced row)

- **A label** is the target that produced a sample, `@<workspace>//<package>:<target>`, its folder its path: the
  timing session `@fsla//measure:session_entmax`, an experiment's run `@fsla//measure/lab:<name>.run`, the oracle tier's
  store `@fsla//measure:store_oracle_tier`, the devbox image's container check `@fsla//:container_check`; flash's
  reference times have a root of their own, `flash/`.
- **A sample** is one execution, one file named by its run, written once (no lock, never rewritten): its semantics and
  their digest, the key, which a reader groups by; its output or its error; when, how long; its provenance (the
  checkouts and commits the tool names; the host); and its parts.
- **A backfilled sample** is a file this repository kept as written before the store held it -- the lab's records,
  each once a file of fsla's `measure/lab/results/` -- its bytes the output unchanged, its date and provenance what the
  file states, marked `backfilled` with the file's old path and the commit it was read at. **A migrated sample** is a
  sample of the store's earlier layout (a record a key under a location), re-filed at its producer's label, its output
  unchanged, marked `migrated` with the record it came from.

Nothing derived from two records (a ratio, a baseline) is stored: that is the reader's. A recorded result is never
rewritten; a new run is a new sample. fsla-devtools' README (`The results store`) is the store's whole contract: what a
record holds, the refusals at the door (a machine path, a timing without its commits), the index's tables and views,
and the verdict.

## Who writes here and who reads it

A tool writes a record through `fsla_devtools.results.Store`, at the checkout the machine's dev config names as
`store.root`, its `records/` the backend. A measurement taken on a rented card comes back as a patch, applied here,
checked by this repository's gate, committed and pushed from the desk -- a rented box never holds push credentials.
fsla pins this repository at ONE commit (fsla-devtools' `environment.data` tag, by the commit's archive digest) and
cites a record by its path inside it (`data:records/fsla/measure/lab/reg_trade.run/20261111T044002Z-68cff01d/output.json`, a
sample's output), so a citation resolves to fixed content; moving the pin to a newer commit is how a new record becomes
citable.

## The gate and the index

    bazel test //:gate        every sample consistent, every path declared, every citation read
    bazel build //:index      the records' SQLite index and views: a build output, never a file beside the records

The gate is the store's own check over `records/` (`python3 -m fsla_devtools.results --root records check`: every
sample is under its label's folder and recomputes its key, its output and parts exist, no lock file is there), the
declaration check (`python -m fsla_devtools.mirror --check`), and the doc references (`//:docrefs`, fsla-devtools'
`fsla_devtools.docrefs`: this README's citations pinned in `references.lock.json`, a `data:` citation resolving in this
checkout, which is the data). Its environment is the standard library and fsla_devtools, from the module's source at the
pinned commit (the front door overrides it with the machine's fsla-devtools checkout). The
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
