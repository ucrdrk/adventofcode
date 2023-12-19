#!/usr/bin/env python3

import sys
import re

word_to_digit = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0}

def convert_word_to_digit(match):
    return str(word_to_digit[match.group()]) + match.group()[1:]

numbers = []
lines = sys.stdin.readlines()
for line in lines:
    while True:
        subbed_line = re.sub('(one|two|three|four|five|six|seven|eight|nine|zero)', convert_word_to_digit, line.strip())
        if subbed_line == line:
            break
        line = subbed_line

    line = re.sub('\D', '', line)
    numbers.append(int(line[0] + line[-1]))
print(sum(numbers))
