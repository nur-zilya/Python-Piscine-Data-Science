#!/bin/bash

INPUT=../ex02/hh_sorted.csv
OUTPUT=hh_positions.csv

head -n 1 $INPUT > $OUTPUT
tail -n 20 $INPUT | \
awk 'BEGIN { FS = OFS = "," }
	{
		STR = ""
		if (index(tolower($3), "junior"))
			STR = STR"Junior/"
		else if (index(tolower($3), "middle"))
			STR = STR"Middle/"
		else if (index(tolower($3), "senior"))
			STR = STR"Senior/"
		else
			STR = "-"
		gsub(/[\/ ]*$/, "", STR)
		$3 = "\""STR"\""
		print
	}' >> $OUTPUT