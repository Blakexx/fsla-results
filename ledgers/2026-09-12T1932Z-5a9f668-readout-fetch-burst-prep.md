# Build ledger 5a9f668 `readout-fetch-burst-prep` (2026-09-12T1932Z)

**SASS** instr 6808 hmma 45 ldl 0 calls 0 predHMMA 0
**Registers** peak live None; by region: 
**Oracle** 88 passed, 0 failed

| cell | head | readout | fold | snapshot | edges | sweep | head_words | head_scans | total | prev total | tensor util (active) | A/B master | this | ratio |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| flagship-dense | 1820 | 53850 | 47685 | 1873 | 1272 | 6030 | 1482 | 544 | 114555 | 114518 | 65% |  |  |  |
| nl64k-alt-k4 | 2503 | 7472 | 7265 | 1649 | 140 | 62 | 1405 | 1601 | 22098 | 22390 | 21% |  |  |  |

**flagship-dense** phase census (a CTA-window; util = HMMA x 32 / 4 / phase cycles; warp cycles split by stall samples at HMMA vs the rest):
| component | cycles | HMMA | util | instr | budget | non-HMMA/HMMA | at HMMA | at other |
|---|---|---|---|---|---|---|---|---|
| ReadoutStream | 53850 | 4608 | 68% | 54412 | 20416 | 10.8 | 27666 | 26184 |
| FoldStream | 47685 | 4608 | 77% | 47042 | 26624 | 9.2 | 21160 | 26525 |
| head | 1820 | 0 | 0% | 4082 | 4008 | 4082.5 | 0 | 1820 |
| snapshot_publish | 1873 | 0 | 0% | 2120 | 944 | 2120.0 | 0 | 1873 |
shared wavefronts above ideal a window: **5674**; by line: L766 3200 (24/instr); L316 960 (16/instr); L1178 768 (16/instr); L770 320 (24/instr); L771 320 (24/instr)

**nl64k-alt-k4** phase census (a CTA-window; util = HMMA x 32 / 4 / phase cycles; warp cycles split by stall samples at HMMA vs the rest):
| component | cycles | HMMA | util | instr | budget | non-HMMA/HMMA | at HMMA | at other |
|---|---|---|---|---|---|---|---|---|
| ReadoutStream | 7472 | 275 | 29% | 6676 |  | 23.3 | 1899 | 5573 |
| FoldStream | 7265 | 297 | 33% | 10218 |  | 33.4 | 1296 | 5969 |
| head | 2503 | 0 | 0% | 3749 |  | 3748.6 | 0 | 2503 |
| snapshot_publish | 1649 | 0 | 0% | 1687 |  | 1687.0 | 0 | 1649 |
shared wavefronts above ideal a window: **7629**; by line: L766 4597 (32/instr); L316 960 (16/instr); L770 462 (32/instr); L771 462 (32/instr); L773 397 (13/instr)

**flagship-dense** components (samples %): ReadoutStream 45.8% (math:49% wait:18% selected:13%  RED > budget 20416.0); FoldStream 41.6% (math:35% wait:31% short_sb:14%  RED > budget 20992.0); carry_kernel 8.9% (wait:22% long_sb:15% selected:15%); FoldStream [spin] 0.1% (short_sb:56% wait:31% mio:12%); head 2.6% (wait:28% barrier:23% short_sb:18%  RED > budget 4008.0); snapshot_publish 1.1% (wait:34% selected:22% mio:21%  RED > budget 944.0)
**nl64k-alt-k4** components (samples %): FoldStream 36.8% (wait:35% math:16% selected:16%); ReadoutStream 25.0% (wait:27% math:26% short_sb:22%); head 18.4% (barrier:45% wait:21% short_sb:16%); carry_kernel 15.1% (wait:28% barrier:20% short_sb:15%); snapshot_publish 4.0% (wait:31% selected:24% mio:17%); FoldStream [spin] 0.7% (short_sb:47% wait:36% selected:10%)

Diff against 5a9f668 `readout-two-deep` (2026-09-12T1927Z):
- flagship-dense: head +9, readout +249, fold -249, snapshot -1, edges -87, sweep +111, head_words -32, head_scans +39
- nl64k-alt-k4: head -3, readout -91, fold -30, snapshot +33, edges -13, sweep +0, head_words +15, head_scans -203
