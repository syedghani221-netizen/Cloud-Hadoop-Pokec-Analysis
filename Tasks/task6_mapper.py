#!/usr/bin/env python3
import sys
ATTRS = {'hobbies':11,'eye_color':16,'hair_color':17,'spoken_languages':10,'favourite_color':21}
for line in sys.stdin:
    cols = line.strip().split('\t')
    if len(cols) < 22:
        continue
    comp = cols[2].strip()
    if not comp.isdigit():
        continue
    for attr, idx in ATTRS.items():
        val = cols[idx].strip()
        status = 'present' if (val and val != 'null') else 'missing'
        sys.stdout.write(attr + '_' + status + '\t' + comp + '\n')

