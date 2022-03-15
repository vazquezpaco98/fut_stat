#!/bin/bash
equipo='BET'
# soccer --team=BET | awk '{ if($3 != "Betis") print $0;}' >> goles_BET_visitante.txt
# soccer --team=BET | awk '{ if($3 != "Betis") print $0;}' >> goles_BET_total.txt
soccer --team=$equipo | awk '{ if($3 == "Betis") print $0;}' | cut -d ' ' -f 12 >> goles_"$equipo"_local.txt
soccer --team=BET | awk '{ if($3 == "Betis") print $0;}' | cut -d ' ' -f 12 >> goles_"$equipo"_total.txt
python3 prueba.py
rm *.txt
