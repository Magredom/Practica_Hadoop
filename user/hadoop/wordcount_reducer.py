#!/usr/bin/env python3

import sys

last_key = None
running_total = 0

for input_line in sys.stdin:
    input_line = input_line.strip()
    this_key, value = input_line.split("\t", 1)
    value = int(value)

    if last_key == this_key:
        running_total += value
    else:
        if last_key:
            print('{0}\t{1}'.format(last_key, running_total))

        running_total = value
        last_key = this_key

if last_key == this_key:
    print('{0}\t{1}'.format(last_key, running_total))
