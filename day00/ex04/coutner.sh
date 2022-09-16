#!/bin/sh
cat ../ex03/hh_positions.csv | grep Junior | cat | wc -l |  cat >> a
v=$(<a)
echo '"Junior",'$v >> hh_uniq_positions1.csv
cat ../ex03/hh_positions.csv | grep Middle | cat | wc -l |  cat >> b
c=$(<b)
echo '"Middle",'$c >> hh_uniq_positions1.csv
cat ../ex03/hh_positions.csv | grep Senior | cat | wc -l |  cat >> x
n=$(<x)
echo '"Senior",'$n >> hh_uniq_positions1.csv


echo '"name","count"' >>  hh_uniq_positions.csv
cat hh_uniq_positions1.csv | sort -t "," -r -nk2   | cat >> hh_uniq_positions.csv

rm -rf a
rm -rf b
rm -rf x
rm -rf hh_uniq_positions1.csv