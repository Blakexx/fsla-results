# The measurements store

Every number the rola tree measures, written by every worktree, host and container into this one git repository
(the rola tree's `store.root`, `tools/dev_config.py`; docs/measurement.md there). Nothing here is written by hand.

    <hw-profile>/<yyyy-mm>/<run_id>.jsonl   the record: one run and its results, provenance in every row
    <hw-profile>/*.json                     reference rows for a card: calibrations, the pipe timeline's scale
    <hw-profile>/environment/<key>.json     dev container checks, by environment key
    ledgers/                                build ledger, composer and timeline reports; the dashboard
    perf/ledger.jsonl                       the bench driver's append-only regression ledger
    .rola/, *.ncu-rep, ledgers/dashboard.html   derived or raw (the index, profiler captures, the page): not committed

Commit with `python tools/dev.py store commit -m <message>` from any rola worktree. Pushing is the owner's act.
