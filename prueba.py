import os
with open("goles_BET_local.txt") as file:
    lines = [line.rstrip('\n') for line in file]

suma = 0

for line in lines:
    line = int(line)
    suma += line

media = (float(suma) / float(len(lines)))


print(media)