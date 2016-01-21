set term postscript eps color enhanced "Arial" 20
set output "cluster.eps"

#set term pngcairo transparent truecolor
#set output "out_pmf.dat.png"

#set title "Free energy landscape"
set nokey

set xlabel "PC1"
set ylabel "PC2"  
#set zlabel "PMF (kcal/mol)"

#set cbrange[0: 10]
#set zrange[0: 10]
#unset ztics
#set xrange[-12:13]
#set yrange[-9 :8 ]

set grid
#set view map

#set palette rgbformulae 33,13,10
#set palette defined (0"black",1"blue",5"cyan",9"orange",13"red",14 "white")


#set label 1 point pt 2 ps 3  at 3.78902, 2.13855 front

unset colorbox

plot "cluster.dat" u 1:2:5 lc palette

set term png
set output "cluster.png"
replot
#pause -1
