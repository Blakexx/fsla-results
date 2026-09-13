# Build ledger 5a9f668 `readout-two-deep` (2026-09-12T1927Z)

**SASS** instr 6864 hmma 54 ldl 0 calls 0 predHMMA 0
**Registers** peak live None; by region: 
**Oracle** 88 passed, 0 failed

| cell | head | readout | fold | snapshot | edges | sweep | head_words | head_scans | total | prev total | tensor util (active) | A/B master | this | ratio |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| flagship-dense | 1811 | 53601 | 47934 | 1874 | 1359 | 5919 | 1514 | 505 | 114518 | None | 65% |  |  |  |
| nl64k-alt-k4 | 2506 | 7563 | 7295 | 1616 | 153 | 62 | 1390 | 1804 | 22390 | None | 20% |  |  |  |

**flagship-dense** phase census (a CTA-window; util = HMMA x 32 / 4 / phase cycles; warp cycles split by stall samples at HMMA vs the rest):
| component | cycles | HMMA | util | instr | budget | non-HMMA/HMMA | at HMMA | at other |
|---|---|---|---|---|---|---|---|---|
| ReadoutStream | 53601 | 4608 | 69% | 52304 | 20416 | 10.4 | 22383 | 31218 |
| FoldStream | 47934 | 4608 | 77% | 46962 | 26624 | 9.2 | 20877 | 27057 |
| head | 1811 | 0 | 0% | 4074 | 4008 | 4074.5 | 0 | 1811 |
| snapshot_publish | 1874 | 0 | 0% | 2120 | 944 | 2120.0 | 0 | 1874 |
shared wavefronts above ideal a window: **5674**; by line: L766 3200 (24/instr); L316 960 (16/instr); L1178 768 (16/instr); L770 320 (24/instr); L771 320 (24/instr)

**nl64k-alt-k4** phase census (a CTA-window; util = HMMA x 32 / 4 / phase cycles; warp cycles split by stall samples at HMMA vs the rest):
| component | cycles | HMMA | util | instr | budget | non-HMMA/HMMA | at HMMA | at other |
|---|---|---|---|---|---|---|---|---|
| ReadoutStream | 7563 | 275 | 29% | 6273 |  | 21.8 | 1839 | 5724 |
| FoldStream | 7295 | 297 | 33% | 10134 |  | 33.1 | 1305 | 5990 |
| head | 2506 | 0 | 0% | 3741 |  | 3740.6 | 0 | 2506 |
| snapshot_publish | 1616 | 0 | 0% | 1687 |  | 1687.0 | 0 | 1616 |
shared wavefronts above ideal a window: **7629**; by line: L766 4597 (32/instr); L316 960 (16/instr); L770 462 (32/instr); L771 462 (32/instr); L773 397 (13/instr)

**flagship-dense** components (samples %): ReadoutStream 46.1% (math:34% wait:30% short_sb:17%  RED > budget 20416.0); FoldStream 41.5% (math:34% wait:33% short_sb:14%  RED > budget 20992.0); FoldStream [spin] 0.1% (short_sb:40% wait:40% selected:15%); carry_kernel 8.7% (wait:24% long_sb:13% no_inst:13%); head 2.6% (wait:27% barrier:26% selected:17%  RED > budget 4008.0); snapshot_publish 1.1% (wait:28% selected:25% mio:17%  RED > budget 944.0)
**nl64k-alt-k4** components (samples %): FoldStream 36.3% (wait:35% math:16% short_sb:16%); ReadoutStream 25.4% (wait:33% math:22% short_sb:22%); head 19.0% (barrier:48% wait:20% short_sb:15%); carry_kernel 14.6% (wait:28% barrier:21% short_sb:15%); snapshot_publish 3.9% (wait:31% selected:24% mio:18%); FoldStream [spin] 0.7% (short_sb:44% wait:38% selected:10%)

Diff against d5d36c5 `fill-rotate-gate` (2026-09-12T1907Z):
