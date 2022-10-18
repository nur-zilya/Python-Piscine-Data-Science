#!/bin/bash

INPUT=../ex01/hh.csv
OUTPUT=hh_sorted.csv

head -n 1 $INPUT > $OUTPUT;
tail -n 20 $INPUT | sort -t, -k2 -k1 >> $OUTPUT;