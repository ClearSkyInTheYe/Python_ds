#/bin/sh

# settings
if [ -z "$1" ]
  then
    INPUT_FILE="../ex02/hh_sorted.csv"  # default
  else
    INPUT_FILE="$1"                     # argument
fi

OUTPUT_FILE="hh_positions.csv"


# pass headers
cat $INPUT_FILE \
  | head -n 1 \
  > $OUTPUT_FILE


# clean up
cat $INPUT_FILE \
  | tail -n +2 \
  | awk \
    'BEGIN{
      FS=OFS="\",";

      R[0] = "[Jj]unior\\ +?/?";
      R[2] = "[Mm]iddle\\ +?/?";
      R[4] = "[Ss]enior";

    }

    {
      result = "";
      for (i = 0; i < length(R); ++i)
      {
        match($3, R[i]);
        if (RLENGTH > 0) {
          first_char = substr($3, RSTART, 1);
          result = result toupper(first_char) substr($3, RSTART + 1, RLENGTH - 1);
        }

      }

      if (length(result) == 0) {
        $3 = "\"-";
      }
      else {
        $3 = "\"" result;
      }

      print;
    }' \
  >> $OUTPUT_FILE

#cleaner()
#{
#  awk -F "\"," 'BEGIN{OFS = FS}{
#  if (tolower($3) ~ "junior" && tolower($3) ~ "middle" && tolower($3) ~ "senior")
#    $3 = "\"Junior/Middle/Senior"
#  else if (tolower($3) ~ "junior" && tolower($3) ~ "middle")
#    $3 = "\"Junior/Middle"
#  else if (tolower($3) ~ "junior" && tolower($3) ~ "senior")
#    $3 = "\"Junior/Senior"
#  else if (tolower($3) ~ "middle" && tolower($3) ~ "senior")
#    $3 = "\"Middle/Senior"
#  else if (tolower($3) ~ "junior")
#    $3 = "\"Junior"
#  else if (tolower($3) ~ "middle")
#    $3 = "\"Middle"
#  else if (tolower($3) ~ "senior")
#    $3 = "\"Senior"
#  else
#    $3 = "\"-"
#  print $0}'
#}
#
## Cleaner without argument
#head -n 1 "../ex02/hh_sorted.csv" > hh_positions.csv
#cat < "../ex02/hh_sorted.csv" | while read -r; do cleaner >> hh_positions.csv; done