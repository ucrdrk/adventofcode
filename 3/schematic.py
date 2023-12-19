#!/usr/bin/env python3

import re
import sys

schematic = []
symbol = re.compile(r'[*$#+]')
for line in sys.stdin.readlines():
    schematic.append([*line.strip()])

rows = len(schematic)
cols = len(schematic[0])

for i in range(0, rows):
    for j in range(0, cols):
        if symbol.match(schematic[i][j]):
            print("Symbol at row " + str(i) + " and col " + str(j))

