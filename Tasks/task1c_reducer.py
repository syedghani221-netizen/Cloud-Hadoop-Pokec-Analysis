#!/usr/bin/env python3
import sys
current_region = None
count = 0
for line in sys.stdin:
    parts = line.strip().split('\t')
    if len(parts) != 2:
        continue
    region = parts[0]
    val = int(parts[1])
    if current_region == region:
        count += val
    else:
        if current_region:
            sys.stdout.write(current_region + '\t' + str(count) + '\n')
        current_region = region
        count = val
if current_region:
    sys.stdout.write(current_region + '\t' + str(count) + '\n')
