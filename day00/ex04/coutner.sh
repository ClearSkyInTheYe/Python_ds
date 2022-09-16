#/bin/sh
echo '"name","count"' >>  hh_uniq_positions.csv
cat ../ex03/hh_positions.csv | grep Junior | cat | wc -l |  cat >> a
v=$(<a)
echo '"Junior"'","$v >> hh_uniq_positions.csv
cat ../ex03/hh_positions.csv | grep Middle | cat | wc -l |  cat >> b
c=$(<b)
echo '"Middle"'","$v >> hh_uniq_positions.csv
cat ../ex03/hh_positions.csv | grep Senior | cat | wc -l |  cat >> x
n=$(<x)
echo '"Senior"'","$v >> hh_uniq_positions.csv
rm -rf a
rm -rf b
rm -rf x