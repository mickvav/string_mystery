set logscale x
set logscale y
set terminal png
set output "plot.png"
set xlabel  "String length"
set ylabel "Time[s]"
plot "pyresult.txt" with lines title "Python", "goresult.txt" with lines title "Golang"
