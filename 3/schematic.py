#!/usr/bin/env python3

import re
import sys

symbol = re.compile(r'[!@#$%^&*\-+=_/]')
digit  = re.compile(r'\d')

def read_part_number(schematic, row, col):
  start = end = col
  for i in range(1, col+1):
    if digit.match(schematic[row][col-i]) != None:
      start -= 1
    else:
      break

  for i in range(1, len(schematic[row])-col):
    if digit.match(schematic[row][col + i]) != None:
      end += 1
    else:
      break
  
  part = "".join(schematic[row][start:end+1])
  schematic[row][start:end+1] = 'X' * len(part)
  return int(part)

def find_part_numbers(schematic, row, col):
  parts = []
  for i in range(-1, 2):
    for j in range(-1, 2):
      if col + j < 0 or col + j >= len(schematic[row]):
        continue
      if row + i >= 0 and row + i < len(schematic) and digit.match(schematic[row + i][col + j]) != None:
        parts.append(read_part_number(schematic, row+i, col+j))
  return parts

schematic = []
for line in sys.stdin.readlines():
  schematic.append([*line])

parts = []
for row in range(0, len(schematic)):
  for col in range(0, len(schematic[row])):
    if symbol.match(schematic[row][col]) != None:
      parts += (find_part_numbers(schematic, row, col))
print(sum(parts))
