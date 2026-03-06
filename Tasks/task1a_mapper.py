#!/usr/bin/env python3
import sys
for line in sys.stdin:
    cols = line.strip().split('\t')
    if len(cols) > 11:
        hobbies = cols[11].strip()
        if hobbies and hobbies != 'null':
            for h in hobbies.lower().split(','):
                h = h.strip()
                if h:
                    sys.stdout.write(h + '\t1\n')
