#!/usr/bin/env python3

import re
import sys
from math import sqrt
from math import floor

times_re = re.compile(r'^Time: ((\s+\d+)+)\s*$')
dists_re = re.compile(r'^Distance: ((\s+\d+)+)\s*$')

def max_time(T):
    return floor(T / 2)

def rec_time(T, d):
    return floor((T - sqrt(T ** 2 - 4 * d)) / 2)

def str_to_list(str):
    return list(map(lambda x : int(x), str.split()))

times = []
distances = []
total_wins = []
for line in sys.stdin.readlines():
    match = times_re.match(line)
    if match != None:
        times = str_to_list(match.group(1))
        continue

    match = dists_re.match(line)
    if match != None:
        distances = str_to_list(match.group(1))

for idx in range(0, len(times)):
    wins = (max_time(times[idx]) - rec_time(times[idx], distances[idx])) * 2 - (1 - (times[idx] % 2))
    total_wins.append(wins)

total = 1
for win in total_wins:
    total *= win

print(total)