# Build ledger 5a9f668 `readout-interleaved` (2026-09-12T1938Z)

**SASS** instr 6864 hmma 54 ldl 0 calls 0 predHMMA 0
**Registers** peak live None; by region: 
**Oracle** 85 passed, 3 failed: tests/oracle/test_carry_vs_oracle.py::test_the_sparse_form_is_the_fp64_reference[flagship-cohort-k4-first], tests/oracle/test_carry_vs_oracle.py::test_the_sparse_form_is_the_fp64_reference[flagship-cohort-k16-first], tests/oracle/test_carry_vs_oracle.py::test_the_sparse_form_is_the_fp64_reference[flagship-cohort-k4-L4096-identity]

| cell | head | readout | fold | snapshot | edges | sweep | head_words | head_scans | total | prev total | tensor util (active) | A/B master | this | ratio |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| flagship-dense | 1894 | 53394 | 48185 | 1971 | 1331 | 6679 | 1471 | 698 | 115622 | 114555 | 64% |  |  |  |
| nl64k-alt-k4 | 2519 | 7934 | 7167 | 1685 | 140 | 63 | 1384 | 1716 | 22609 | 22098 | 22% |  |  |  |

**flagship-dense** phase census (a CTA-window; util = HMMA x 32 / 4 / phase cycles; warp cycles split by stall samples at HMMA vs the rest):
| component | cycles | HMMA | util | instr | budget | non-HMMA/HMMA | at HMMA | at other |
|---|---|---|---|---|---|---|---|---|
| ReadoutStream | 53394 | 4608 | 69% | 49848 | 20416 | 9.8 | 28579 | 24815 |
| FoldStream | 48185 | 4608 | 77% | 47256 | 26624 | 9.3 | 21959 | 26226 |
| head | 1894 | 0 | 0% | 4095 | 4008 | 4095.0 | 0 | 1894 |
| snapshot_publish | 1971 | 0 | 0% | 2116 | 944 | 2116.0 | 0 | 1971 |
shared wavefronts above ideal a window: **5674**; by line: L766 3360 (24/instr); L316 960 (16/instr); L1178 768 (16/instr); L770 480 (24/instr); L432 64 (5/instr)

**nl64k-alt-k4** phase census (a CTA-window; util = HMMA x 32 / 4 / phase cycles; warp cycles split by stall samples at HMMA vs the rest):
| component | cycles | HMMA | util | instr | budget | non-HMMA/HMMA | at HMMA | at other |
|---|---|---|---|---|---|---|---|---|
| ReadoutStream | 7934 | 311 | 31% | 6707 |  | 20.6 | 2210 | 5724 |
| FoldStream | 7167 | 297 | 33% | 10137 |  | 33.2 | 1182 | 5985 |
| head | 2519 | 0 | 0% | 3742 |  | 3742.0 | 0 | 2519 |
| snapshot_publish | 1685 | 0 | 0% | 1687 |  | 1686.9 | 0 | 1685 |
shared wavefronts above ideal a window: **7629**; by line: L766 5440 (32/instr); L316 960 (16/instr); L773 397 (13/instr); L1178 199 (17/instr); L954 193 (7/instr)

**flagship-dense** components (samples %): ReadoutStream 45.5% (math:50% wait:22% selected:12%  RED > budget 20416.0); FoldStream 41.2% (math:36% wait:33% short_sb:13%  RED > budget 20992.0); carry_kernel 9.4% (wait:21% long_sb:15% barrier:14%); FoldStream [spin] 0.0% (wait:64% short_sb:18% not_selected:9%); head 2.7% (wait:29% barrier:28% selected:16%  RED > budget 4008.0); snapshot_publish 1.1% (wait:33% selected:23% mio:20%  RED > budget 944.0)
**nl64k-alt-k4** components (samples %): FoldStream 36.1% (wait:37% selected:15% short_sb:15%); ReadoutStream 26.0% (wait:30% math:27% short_sb:17%); head 18.5% (barrier:47% wait:21% short_sb:16%); carry_kernel 14.5% (wait:26% barrier:20% short_sb:16%); snapshot_publish 4.2% (wait:30% selected:22% mio:19%); FoldStream [spin] 0.7% (short_sb:50% wait:32% selected:11%)

Diff against 5a9f668 `readout-fetch-burst-prep` (2026-09-12T1932Z):
- flagship-dense: head +74, readout -456, fold +500, snapshot +98, edges +59, sweep +649, head_words -11, head_scans +154
- nl64k-alt-k4: head +16, readout +462, fold -98, snapshot +36, edges +0, sweep +1, head_words -21, head_scans +115
