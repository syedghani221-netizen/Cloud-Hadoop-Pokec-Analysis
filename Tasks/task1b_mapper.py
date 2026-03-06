#!/usr/bin/env python3
import sys
for line in sys.stdin:
    cols = line.strip().split('\t')
    if len(cols) > 16:
        completion = cols[2].strip()
        eye = cols[16].strip()
        if eye and eye != 'null' and completion.isdigit():
            sys.stdout.write(eye + '\t' + completion + '\n')
