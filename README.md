# diodes-Inc2LTSpice
Convert diodes Inc BJT transistor spice models to .\LTspiceXVII\lib\cmp\standard.bjt

Input: "Transistor (BJT) Master Table.spice.txt" file
Input: "Transistor (BJT) Master Table.csv"

Remove spurious subckt ends, scrape csv file for Vceo, Icrating for LT parametric search

cat out.txt >> .\LTspiceXVII\lib\cmp\standard.bjt
