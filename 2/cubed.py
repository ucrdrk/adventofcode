#!/usr/bin/env python3

import re
import sys

bag = {'red': 12, 'green': 13, 'blue': 14}

valid_games = []

for line in sys.stdin.readlines():
    game_number_match = re.search("Game (\d+):\s+", line.strip())
    game_number = int(game_number_match.group(1))
    tries = re.split(r'[,;]\s+', line.strip()[game_number_match.end():])
    possible = True
    for t in tries:
        count, color = re.split(r'\s+', t)
        if int(count) > bag[color]:
            possible = False
            break
    if possible:
        valid_games.append(game_number)

print(sum(valid_games))