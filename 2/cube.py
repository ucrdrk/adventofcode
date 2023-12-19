#!/usr/bin/env python3

import re
import sys

game_header = re.compile('Game (\d+):\s+')

bag = {'blue': 14, 'red': 12, 'green': 13}
games = []
for line in sys.stdin.readlines():
  match = game_header.match(line)
  game_number = int(match.group(1))
  trys = re.split(r'[,;]\s+', line.strip()[match.end():])
  possible = True
  for t in trys:
    count, color = t.split()
    if int(count) > bag[color]:
      possible = False
      break
  if possible:
    games.append(game_number)
print(sum(games))
