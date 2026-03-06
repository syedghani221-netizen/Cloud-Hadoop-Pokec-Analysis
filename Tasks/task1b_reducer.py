#!/usr/bin/env python3
import sys
current_eye = None
total = 0
count = 0
for line in sys.stdin:
    parts = line.strip().split('\t')
    if len(parts) != 2:
        continue
    eye = parts[0]
    comp = float(parts[1])
    if current_eye == eye:
        total += comp
        count += 1
    else:
        if current_eye:
            sys.stdout.write(current_eye + '\t' + str(round(total/count,2)) + '\n')
        current_eye = eye
        total = comp
        count = 1
if current_eye:
    sys.stdout.write(current_eye + '\t' + str(round(total/count,2)) + '\n')
