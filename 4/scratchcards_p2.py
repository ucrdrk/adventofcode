#!/usr/bin/env python3

import re
import sys

card = re.compile(r'Card\s+(\d+):\s+')
winning = re.compile(r'((\d+\s*)+)\s+\|')
yours   = re.compile(r'\|\s*((\d+\s*)+)')

lines = sys.stdin.readlines()
counts = [1] * len(lines)
for line in lines:
    card_no = int(card.match(line).group(1)) - 1
    winners =  set(re.split(r'\s+', winning.search(line).group(1)))
    your_numbers = set(re.split(r'\s+', yours.search(line.strip()).group(1)))

    winning_numbers = len(list(winners & your_numbers))
    if winning_numbers > 0:
        for idx in range(1, winning_numbers+1):
            counts[card_no+idx] += counts[card_no]

print(sum(counts))