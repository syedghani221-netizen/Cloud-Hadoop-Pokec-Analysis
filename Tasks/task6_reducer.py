#!/usr/bin/env python3
import sys
current_key = None
total = 0
count = 0
for line in sys.stdin:
    parts = line.strip().split('\t')
    if len(parts) != 2:
        continue
    key = parts[0]
    val = float(parts[1])
    if current_key == key:
        total += val
        count += 1
    else:
        if current_key:
            sys.stdout.write(current_key + '\tcount=' + str(count) + '\tavg=' + str(round(total/count,2)) + '\n')
        current_key = key
        total = val
        count = 1
if current_key:
    sys.stdout.write(current_key + '\tcount=' + str(count) + '\tavg=' + str(round(total/count,2)) + '\n')
