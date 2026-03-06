#!/usr/bin/env python3
import sys
for line in sys.stdin:
    cols = line.strip().split('\t')
    if len(cols) > 4:
        region = cols[4].strip()
        if region and region != 'null':
            sys.stdout.write(region + '\t1\n')
