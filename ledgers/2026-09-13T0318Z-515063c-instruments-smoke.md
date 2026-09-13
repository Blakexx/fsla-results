# Build ledger 515063c `instruments-smoke` (2026-09-13T0318Z)

**SASS** instr 6744 hmma 45 ldl 0 calls 0 predHMMA 0
**Registers** peak live 169; by region: FoldStream::FoldStream 142, FoldStream::step 124, FoldStream::try_fill 103, FoldStream::wait 63, PhaseClock::PhaseClock 118, PhaseClock::lap 142, PoolCursor::empty_now 103, PoolCursor::filled 140
**Oracle** None passed, None failed

| cell | head | readout | fold | snapshot | edges | sweep | head_words | head_scans | total | prev total | tensor util (active) | A/B master | this | ratio |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| flagship-dense | 1812 | 51867 | 46289 | 1872 | 1338 | 4620 | 1481 | 455 | 109734 | 112149 | 66% |  |  |  |


**flagship-dense** phase census (a CTA-window; util = HMMA x 32 / 4 / phase cycles; warp cycles split by stall samples at HMMA vs the rest):
| component | cycles | HMMA | util | instr | budget | non-HMMA/HMMA | at HMMA | at other |
|---|---|---|---|---|---|---|---|---|
| ReadoutStream | 51867 | 4608 | 71% | 44524 | 20416 | 8.7 | 24531 | 27336 |
| FoldStream | 46289 | 4608 | 80% | 46896 | 26624 | 9.2 | 21259 | 25030 |
| head | 1812 | 0 | 0% | 4074 | 4008 | 4073.5 | 0 | 1812 |
| snapshot_publish | 1872 | 0 | 0% | 2072 | 944 | 2072.0 | 0 | 1872 |
shared wavefronts above ideal a window: **5673.5**; by line: L784 3200.0 (24/instr); L334 960.0 (16/instr); L1232 768.0 (16/instr); L788 320.0 (24/instr); L789 320.0 (24/instr)

**flagship-dense** components (samples %): FoldStream 41.5% (math:37% wait:33% short_sb:12%); ReadoutStream 44.7% (math:40% wait:24% short_sb:19%); carry_kernel 10.0% (wait:29% selected:13% no_inst:12%); FoldStream [spin] 0.1% (short_sb:44% wait:44% branch_resolving:6%); head 2.5% (wait:27% barrier:20% short_sb:19%); snapshot_publish 1.1% (wait:32% selected:22% mio:20%)

Diff against 5a9f668 `readout-rows-overlap` (2026-09-12T2049Z):
- flagship-dense: head -94, readout +1047, fold -1389, snapshot -92, edges -2, sweep -1409, head_words -452, head_scans -25
