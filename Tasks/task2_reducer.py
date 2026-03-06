#!/usr/bin/env python3
import sys
from collections import defaultdict
lang_counts = defaultdict(int)
user_ids = []
for line in sys.stdin:
    parts = line.strip().split('\t')
    if len(parts) != 3:
        continue
    type_ = parts[0]
    key = parts[1]
    val = int(parts[2])
    if type_ == 'USERID':
        user_ids.append(int(key))
    elif type_ == 'LANG':
        lang_counts[key] += val
sys.stdout.write('=== Task 2: user_id Analysis ===\n')
if user_ids:
    sys.stdout.write('Total Users : ' + str(len(user_ids)) + '\n')
    sys.stdout.write('Min user_id : ' + str(min(user_ids)) + '\n')
    sys.stdout.write('Max user_id : ' + str(max(user_ids)) + '\n')
sys.stdout.write('\n=== Top 10 Spoken Languages ===\n')
for lang, cnt in sorted(lang_counts.items(), key=lambda x: -x[1])[:10]:
    sys.stdout.write(lang + '\t' + str(cnt) + '\n')
