# Build ledger 7cd5e1f `edcab3e-baseline` (2026-09-12T0818Z)

**SASS** instr 6584 hmma 45 ldl 0 calls 0 predHMMA 0
**Registers** peak live 168; by region: window_loop 168, pool_fill 162, chan_row_off 161, box_words 161, head 160, snapshot_publish 157, row32_off 155, pool_inner_off 151
**Oracle** 88 passed, 0 failed

| cell | head | readout | fold | snapshot | edges | sweep | total | prev total | tensor util (active) | A/B master | this | ratio |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| nl64k-alt-k4 | 5467 | 7382 | 7280 | 2975 | 252 | 83 | 23439 | None | 19% | 6.954 | 7.2417 | 1.041 |
| flagship-dense | 3726 | 52086 | 47550 | 2479 | 1245 | 6571 | 113657 | None | 65% | 0.5263 | 0.5437 | 1.033 |
| flagship-alt-k4 | 4339 | 7447 | 7072 | 3027 | 1373 | 6853 | 30112 | None | 15% | 0.1485 | 0.1505 | 1.013 |
| flagship-cohort-k4 | 4068 | 2026 | 1891 | 1349 | 1170 | 6135 | 16639 | None | 10% | 0.1014 | 0.086 | 0.848 |

**nl64k-alt-k4** components (samples %): FoldStream 34.5% (wait:37% math:16% selected:16%); ReadoutStream 22.8% (wait:30% math:24% short_sb:22%); carry_kernel 15.7% (wait:26% barrier:21% short_sb:19%); head 17.2% (barrier:46% wait:21% short_sb:15%); snapshot_publish 9.0% (mio:59% short_sb:14% wait:11%); FoldStream [spin] 0.7% (short_sb:45% wait:39% selected:10%)
**flagship-dense** components (samples %): FoldStream 41.5% (math:36% wait:33% short_sb:11%  RED > budget 20992.0); ReadoutStream 44.1% (math:48% wait:22% short_sb:13%  RED > budget 17600.0); FoldStream [spin] 0.1% (short_sb:56% wait:33% mio:4%); carry_kernel 10.7% (wait:26% barrier:19% long_sb:11%); head 2.5% (wait:30% barrier:23% selected:17%  RED > budget 4008.0); snapshot_publish 1.0% (wait:31% mio:21% selected:21%  RED > budget 944.0)
**flagship-alt-k4** components (samples %): FoldStream 30.8% (wait:33% selected:15% short_sb:13%  RED > budget 3872.0); carry_kernel 26.1% (barrier:17% long_sb:16% wait:15%); ReadoutStream 20.0% (wait:31% short_sb:25% math:22%  RED > budget 1916.0); head 12.3% (barrier:30% short_sb:24% wait:24%  RED > budget 4008.0); snapshot_publish 10.4% (mio:59% short_sb:15% wait:10%  RED > budget 944.0); FoldStream [spin] 0.4% (short_sb:39% wait:33% branch_resolving:15%)
**flagship-cohort-k4** components (samples %): carry_kernel 41.8% (barrier:24% wait:15% selected:14%); head 20.4% (barrier:26% wait:22% short_sb:19%  RED > budget 4008.0); ReadoutStream 12.0% (short_sb:29% wait:29% math:16%  RED > budget 0.0); FoldStream 16.5% (mio:29% wait:25% math:18%  RED > budget 1472.0); snapshot_publish 9.0% (mio:47% wait:16% short_sb:14%  RED > budget 944.0); FoldStream [spin] 0.3% (short_sb:31% wait:31% branch_resolving:23%)

Diff against edcab3e `dryrun` (2026-09-12T0800Z):
