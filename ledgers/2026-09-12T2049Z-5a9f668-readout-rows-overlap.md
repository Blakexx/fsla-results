# Build ledger 5a9f668 `readout-rows-overlap` (2026-09-12T2049Z)

**SASS** instr 7360 hmma 81 ldl 0 calls 0 predHMMA 0
**Registers** peak live None; by region: 
**Oracle** 88 passed, 0 failed

| cell | head | readout | fold | snapshot | edges | sweep | head_words | head_scans | total | prev total | tensor util (active) | A/B master | this | ratio |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| flagship-dense | 1906 | 50820 | 47678 | 1964 | 1340 | 6029 | 1933 | 480 | 112149 | 115622 | 66% |  |  |  |
| nl64k-alt-k4 | 2459 | 7227 | 7373 | 1683 | 140 | 61 | 1393 | 1637 | 21972 | 22609 | 21% |  |  |  |

**flagship-dense** phase census (a CTA-window; util = HMMA x 32 / 4 / phase cycles; warp cycles split by stall samples at HMMA vs the rest):
| component | cycles | HMMA | util | instr | budget | non-HMMA/HMMA | at HMMA | at other |
|---|---|---|---|---|---|---|---|---|
| ReadoutStream | 50820 | 4608 | 73% | 43972 | 20416 | 8.5 | 23974 | 26846 |
| FoldStream | 47678 | 4608 | 77% | 48279 | 26624 | 9.5 | 20666 | 27012 |
| head | 1906 | 0 | 0% | 4122 | 4008 | 4122.5 | 0 | 1906 |
| snapshot_publish | 1964 | 0 | 0% | 2156 | 944 | 2156.0 | 0 | 1964 |
shared wavefronts above ideal a window: **5674**; by line: L766 3200 (24/instr); L316 960 (16/instr); L1178 768 (16/instr); L770 320 (24/instr); L771 320 (24/instr)

**nl64k-alt-k4** phase census (a CTA-window; util = HMMA x 32 / 4 / phase cycles; warp cycles split by stall samples at HMMA vs the rest):
| component | cycles | HMMA | util | instr | budget | non-HMMA/HMMA | at HMMA | at other |
|---|---|---|---|---|---|---|---|---|
| ReadoutStream | 7227 | 275 | 30% | 3600 |  | 12.1 | 2556 | 4671 |
| FoldStream | 7373 | 297 | 32% | 10262 |  | 33.6 | 1298 | 6075 |
| head | 2459 | 0 | 0% | 3820 |  | 3820.1 | 0 | 2459 |
| snapshot_publish | 1683 | 0 | 0% | 1711 |  | 1711.1 | 0 | 1683 |
shared wavefronts above ideal a window: **7629**; by line: L766 4597 (32/instr); L316 960 (16/instr); L770 462 (32/instr); L771 462 (32/instr); L773 397 (13/instr)

**flagship-dense** components (samples %): FoldStream 42.6% (math:34% wait:34% selected:12%  RED > budget 20992.0); ReadoutStream 42.9% (math:40% wait:25% short_sb:19%  RED > budget 20416.0); carry_kernel 10.7% (wait:25% short_sb:14% selected:13%); FoldStream [spin] 0.1% (short_sb:59% wait:24% no_inst:12%); head 2.8% (wait:29% short_sb:19% selected:18%  RED > budget 4008.0); snapshot_publish 0.9% (wait:26% mio:22% selected:20%  RED > budget 944.0)
**nl64k-alt-k4** components (samples %): FoldStream 37.0% (wait:36% math:16% selected:16%); carry_kernel 24.0% (wait:33% short_sb:22% selected:14%); head 18.7% (barrier:45% wait:21% short_sb:16%); ReadoutStream 15.4% (math:30% wait:28% short_sb:21%); snapshot_publish 4.1% (wait:31% selected:23% mio:16%); FoldStream [spin] 0.7% (short_sb:46% wait:37% selected:9%)

Diff against 5a9f668 `readout-interleaved` (2026-09-12T1938Z):
- flagship-dense: head +12, readout -2574, fold -507, snapshot -7, edges +9, sweep -650, head_words +462, head_scans -218
- nl64k-alt-k4: head -60, readout -707, fold +206, snapshot -2, edges +0, sweep -2, head_words +9, head_scans -79
