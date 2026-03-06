#!/usr/bin/env python3
import sys
current_grp = None
values = []
for line in sys.stdin:
    parts = line.strip().split('\t')
    if len(parts) != 2:
        continue
    grp = parts[0]
    val = float(parts[1])
    if current_grp == grp:
        values.append(val)
    else:
        if current_grp and values:
            avg = sum(values)/len(values)
            sys.stdout.write(current_grp + '\tcount=' + str(len(values)) + '\tavg=' + str(round(avg,2)) + '\n')
        current_grp = grp
        values = [val]
if current_grp and values:
    avg = sum(values)/len(values)
    sys.stdout.write(current_grp + '\tcount=' + str(len(values)) + '\tavg=' + str(round(avg,2)) + '\n')
