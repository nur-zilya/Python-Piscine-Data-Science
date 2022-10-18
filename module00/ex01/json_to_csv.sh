#!/bin/sh

#bash "../ex00/hh.sh"
jq -rf filter.jq "../ex00/hh.json" > hh.csv

