#!/usr/bin/env python3
import sys
current_word = None
current_count = 0
for line in sys.stdin:
    parts = line.strip().split('\t')
    if len(parts) != 2:
        continue
    word = parts[0]
    count = int(parts[1])
    if current_word == word:
        current_count += count
    else:
        if current_word:
            sys.stdout.write(str(current_count) + '\t' + current_word + '\n')
        current_word = word
        current_count = count
if current_word:
    sys.stdout.write(str(current_count) + '\t' + current_word + '\n')
