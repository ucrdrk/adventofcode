#!/usr/bin/env python3

import re
import sys

word_to_digit = {'zero':0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight':8, 'nine': 9}

def convert_word_to_digit(match):
  group = match.group(1)
  return str(word_to_digit[group]) + group[1:]

numbers = []
for line in (sys.stdin.readlines()):
  while True:
    subbed_line = re.sub('(zero|one|two|three|four|five|six|seven|eight|nine)', convert_word_to_digit, line)
    if subbed_line == line:
      break
    line = subbed_line
  line = re.sub('(\D)*', '', line)
  numbers.append(int(line[0] + line[-1]))

print(sum(numbers))#!/usr/bin/env python3

