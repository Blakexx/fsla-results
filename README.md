# rola-results

The interface every rola tool stores its measurements through (`rola_results`), and, by default, the records themselves.

```python
from rola_results import Store, checkout

store = Store("probe_cells")                       # the tool's own location
semantics = {"bench": "prefill_op", "cell": "nl64k-alt-k4", "binary": so_sha256, "instrument": code_key}
store.put(semantics, output=rows, wall_s=12.3, provenance=checkout(worktree))
store.put(semantics, error="RuntimeError: ...")    # a failure is a sample too
record = store.get(key(semantics))                  # Store.complete(record), store.output(record)
```

- **A location** names who stores: `probe_cells`, `bench_driver`, `suite/carry.sass`.
- **A record** is everything kept under one key: the semantics the tool handed over and every sample.
- **The key** is sha256 over the semantics, so a repeat lands on the same record and a changed input on a new one.
- **A sample** is one execution: its output (JSON, or a file moved in) or its error, when, how long, its provenance
  (the checkouts and commits the tool names; the host).

Nothing derived from two records (a ratio, a baseline) is stored: that is the reader's.

    records/<location>/<key>.json            the record
    records/<location>/<key>.<n>.out.<ext>   sample n's output

The rola tree names this checkout as `store.root` in its dev config, and `tools/dev.py init` makes the package importable
from every interpreter it provisions.

    python -m rola_results check              every key recomputes, every location is its directory, every output exists
    python -m rola_results show [LOCATION]
    python -m rola_results commit -m MESSAGE  commits records/ only; the library goes through its gated commits

The commit gate (`.githooks/pre-commit`, `core.hooksPath`): ruff and the contract tests on the library, `check` on the
records. Pushing is the owner's act.
