set terminal canvas jsdir ""
set output "/tmp/quast_results/results_2022_03_05_20_55_21/contigs_reports/nucmer_output/de_novo_out.html"
set xtics rotate ( \
 "0" 0, \
 "200000" 200000, \
 "400000" 400000, \
 "600000" 600000, \
 "800000" 800000, \
 "1000000" 1000000, \
 "1200000" 1200000, \
 "1400000" 1400000, \
 "1600000" 1600000, \
 "" 1637762 \
)
set ytics ( \
 "0" 0, \
 "400000" 400000, \
 "800000" 800000, \
 "1200000" 1200000, \
 "1600000" 1600000, \
 "2000000" 2000000, \
 "2400000" 2400000, \
 "2800000" 2800000, \
 "3200000" 3200000, \
 "" 3213335 \
)
set size 1,1
set grid
set key outside bottom right
set border 0
set tics scale 0
set xlabel "Reference" noenhanced
set ylabel "Assembly" noenhanced
set format "%.0f"
set xrange [1:1637762]
set yrange [1:3213335]
set linestyle 1  lt 1 lc rgb "red" lw 3 pt 7 ps 0.5
set linestyle 2  lt 3 lc rgb "blue" lw 3 pt 7 ps 0.5
set linestyle 3  lt 2 lc rgb "yellow" lw 3 pt 7 ps 0.5
plot \
 "/tmp/quast_results/results_2022_03_05_20_55_21/contigs_reports/nucmer_output/de_novo_out.fplot" title "FWD" w lp ls 1, \
 "/tmp/quast_results/results_2022_03_05_20_55_21/contigs_reports/nucmer_output/de_novo_out.rplot" title "REV" w lp ls 2
