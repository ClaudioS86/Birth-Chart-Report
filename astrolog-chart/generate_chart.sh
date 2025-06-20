#!/bin/bash

DATE=$1       # formato: DD/MM/YYYY
TIME=$2       # formato: HH:MM
LAT=$3
LON=$4
TZ=$5
LOCATION=$6
OUTFILE=$7

# Estrai giorno, mese, anno
DAY=$(echo $DATE | cut -d'/' -f1)
MONTH=$(echo $DATE | cut -d'/' -f2)
YEAR=$(echo $DATE | cut -d'/' -f3)

# Estrai ora e minuti
HOUR=$(echo $TIME | cut -d':' -f1)
MINUTE=$(echo $TIME | cut -d':' -f2)

# Genera immagine
astrolog -q -X -i -z$TZ -n"$LOCATION" -y $YEAR -m $MONTH -d $DAY -h $HOUR -n $MINUTE -l $LAT -L $LON -o $OUTFILE
