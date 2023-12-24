#!/usr/bin/env python3

import re
import sys

seeds = re.compile(r'^seeds:\s+((\d+\s*)*)$')
map_to = re.compile(r'^(\w+\-to\-\w+)\s+map:\s*$')
map_values = re.compile(r'^((\d+\s*)+)$')
maps = {}
curr_map = ''

needs_planting = []

for line in sys.stdin.readlines():
    line = line.strip()
    seeds_match = seeds.match(line)
    if seeds_match != None:
        needs_planting = list(map(lambda x : int(x), seeds_match.group(1).split()))
        continue

    map_to_match = map_to.match(line)
    if map_to_match != None:
        curr_map = map_to_match.group(1)
        maps[curr_map] = []
        continue

    map_values_match = map_values.match(line)
    if map_values_match != None:
        maps[curr_map].append(list(map(lambda x : int(x), map_values_match.group(1).split())))

location = sys.maxsize
for start in range(0, len(needs_planting), 2):
    print('Processing range ', needs_planting[start], ' to ', (needs_planting[start] + needs_planting[start+1]))
    seed = needs_planting[start]
    for idx in range(seed, seed + needs_planting[start+1]):
        index = idx
        for map_key in maps:
            for mapping in maps[map_key]:
                if index >= mapping[1] and index < mapping[1] + mapping[2]:
                    index = mapping[0] + (index - mapping[1])
                    break
        if index < location: 
            location = index

print(min(location))
