#!/usr/bin/env python3

import re
import sys

numbers = []
for line in sys.stdin.readlines():
  line = re.sub(r'(\D+)', '', line)
  numbers.append(int(line[0] + line[-1]))
print(sum(numbers))
#!/usr/bin/env python3

import sys
import re

sum = 0
lines = sys.stdin.readlines()
for line in lines:
    line = re.sub('\D+', '', line)
    sum += int(line[0] + line[-1])
print(sum)