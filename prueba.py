import os
with open("BET.txt") as file:
    lines = file.readlines()

for line in lines:
    print(line + 1)