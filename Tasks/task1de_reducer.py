#!/usr/bin/env python3
import sys
from collections import defaultdict
age_counts = defaultdict(int)
eye_counts = defaultdict(int)
for line in sys.stdin:
    parts = line.strip().split('\t')
    if len(parts) != 3:
        continue
    type_ = parts[0]
    key = parts[1]
    val = int(parts[2])
    if type_ == 'AGE':
        age_counts[key] += val
    elif type_ == 'EYE':
        eye_counts[key] += val
sys.stdout.write('=== Task 1d: Age Groups ===\n')
for g in ['under_18','18_to_25','26_to_35','36_to_50','above_50']:
    c = age_counts.get(g, 0)
    flag = ' <-- ZERO USERS' if c == 0 else ''
    sys.stdout.write(g + '\t' + str(c) + flag + '\n')
sys.stdout.write('\n=== Task 1e: Eye Color Frequency ===\n')
for eye, cnt in sorted(eye_counts.items(), key=lambda x: x[1]):
    sys.stdout.write(eye + '\t' + str(cnt) + '\n')
