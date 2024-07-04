set logscale x
set logscale y
set terminal png
set output "plot.png"
plot "pyresult.txt" with lines, "goresult.txt" with lines
