#!/usr/bin/env python3

import re
import sys

numbers = []
for line in sys.stdin.readlines():
  line = re.sub(r'(\D+)', '', line)
  numbers.append(int(line[0] + line[-1]))
print(sum(numbers))
