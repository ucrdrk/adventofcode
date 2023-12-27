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

def str_to_num(str):
    num = ''
    for n in str.split():
        num += n
    return int(num)

times = []
distances = []
total_wins = []
for line in sys.stdin.readlines():
    match = times_re.match(line)
    if match != None:
        times = str_to_num(match.group(1))
        continue

    match = dists_re.match(line)
    if match != None:
        distances = str_to_num(match.group(1))

wins = (max_time(times) - rec_time(times, distances)) * 2 - (1 - (times % 2))
print(wins)