#!/usr/bin/env python3

import re
import sys

card = re.compile(r'Card\s+(\d+):\s+')
winning = re.compile(r'((\d+\s*)+)\s+\|')
yours   = re.compile(r'\|\s*((\d+\s*)+)')

scores = []
for line in sys.stdin.readlines():
    card_no = card.match(line).group(1)
    winners =  set(re.split(r'\s+', winning.search(line).group(1)))
    your_numbers = set(re.split(r'\s+', yours.search(line.strip()).group(1)))

    winning_numbers = len(list(winners & your_numbers))
    if winning_numbers > 0:
        scores.append(2 ** (winning_numbers-1))

print(sum(scores))