#!/usr/bin/env python3
import sys
for line in sys.stdin:
    cols = line.strip().split('\t')
    if len(cols) > 21:
        uid = cols[0].strip()
        comp = cols[2].strip()
        region = cols[4].strip()
        color = cols[21].strip()
        if uid.isdigit() and comp.isdigit() and region and region != 'null' and color and color != 'null':
            key = color.lower() + '_' + region.lower()
            sys.stdout.write(key + '\t' + uid + ',' + comp + '\n')
