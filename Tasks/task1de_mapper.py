#!/usr/bin/env python3
import sys
for line in sys.stdin:
    cols = line.strip().split('\t')
    if len(cols) > 16:
        age = cols[7].strip()
        eye = cols[16].strip()
        if age.isdigit():
            a = int(age)
            if a < 18: grp = 'under_18'
            elif a <= 25: grp = '18_to_25'
            elif a <= 35: grp = '26_to_35'
            elif a <= 50: grp = '36_to_50'
            else: grp = 'above_50'
            sys.stdout.write('AGE\t' + grp + '\t1\n')
        if eye and eye != 'null':
            sys.stdout.write('EYE\t' + eye.lower() + '\t1\n')
