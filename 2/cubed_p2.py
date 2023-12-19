#!/usr/bin/env python3

import re
import sys

bag = {'red': 12, 'green': 13, 'blue': 14}

cubes = []

for line in sys.stdin.readlines():
    game_number_match = re.search("Game (\d+):\s+", line.strip())
    game_number = int(game_number_match.group(1))
    tries = re.split(r'[,;]\s+', line.strip()[game_number_match.end():])
    mins ={'red': 0, 'green': 0, 'blue': 0}
    for t in tries:
        count, color = re.split(r'\s+', t)
        count = int(count)
        if count > mins[color]:
            mins[color] = count
    cubes.append(mins['red'] * mins['green'] * mins['blue'])   

print(sum(cubes))