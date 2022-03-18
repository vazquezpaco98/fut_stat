import os

equipos_code = ["BAY", "HSV", "FCA", "BSC", "B04", "TSG", "DAR", "H96", "M05", "FCI", "SVW", "S04", "BVB", "BMG", "WOB", "SGE", "VFB", "FCK", "null", "PFC", "EVA", "FCM", "RCL", "SUSFC", "PSV", "ROM", "JUVE", "PAL", "GEN", "SASS", "SSC", "LAZ", "INT", "FCT", "FIO", "ACM", "EMP", "KAI", "EBS", "SVS", "SCF", "FCN", "FSV", "RBL", "GRE", "KAR", "HEI", "1860", "PAD", "VFL", "FCP", "FCU", "FOR", "MUFC", "THFC", "AFCB", "AVFC", "EFC", "WAT", "LCFC", "SUN", "NCFC", "CRY", "CFC", "SWA", "NUFC", "SFC", "AFC", "WHU", "SCFC", "LFC", "WBA", "MCFC", "MFF", "ASTA", "GSK", "CSK", "SHA", "ZEN", "DYK", "MTA", "OLA", "DIN", "AUE", "VFR", "OSC", "PSG", "MAR", "SMC", "NIC", "MON", "NAN", "GUI", "MHSC", "SCB", "REN", "BOR", "REI", "TOU", "ETI", "OLY", "LOR", "CFE", "UDA", "CCF", "LAC", "RSS", "ESP", "FCG", "ATM", "RAY", "VAL", "MAL", "SEV", "BIL", "FCB", "MAD", "LUD", "VIG", "BET", "VCF", "GCF", "EIB", "SCP", "SLB"]



#sacar las parejas nombre codigo


with open("parejas.txt") as file:
    lines = [line.rstrip('\n') for line in file]

parejas = []
for line in lines:
    if line.split(':', 3) != '':
        pareja = line.split(':' , 3)
        if (len(pareja[0]) < 4 and len(pareja[0]) > 2):
            parejas.append(line.split(':', 3))

for pareja in parejas:
     print(pareja[0])

#CALCULAR MEDIA DE GOLES A PARTIR DE UN ARCHIVO
for code in equipos_code:
    with open("goles_"+code+"local.txt") as file:
        lines = [line.rstrip('\n') for line in file]
    suma = 0

    for line in lines:
        line = int(line)
        suma += line

    media = (float(suma) / float(len(lines)))
    print(media)
