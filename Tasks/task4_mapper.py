#!/usr/bin/env python3
import sys
for line in sys.stdin:
    cols = line.strip().split('\t')
    if len(cols) > 7:
        age = cols[7].strip()
        comp = cols[2].strip()
        if age.isdigit() and comp.isdigit():
            a = int(age)
            if a < 18: grp = 'A_under_18'
            elif a <= 25: grp = 'B_18_to_25'
            elif a <= 35: grp = 'C_26_to_35'
            elif a <= 50: grp = 'D_36_to_50'
            else: grp = 'E_above_50'
            sys.stdout.write(grp + '\t' + comp + '\n')
