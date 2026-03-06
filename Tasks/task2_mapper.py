#!/usr/bin/env python3
import sys
for line in sys.stdin:
    cols = line.strip().split('\t')
    if len(cols) > 10:
        user_id = cols[0].strip()
        lang = cols[10].strip()
        if user_id.isdigit():
            sys.stdout.write('USERID\t' + user_id + '\t1\n')
        if lang and lang != 'null':
            for l in lang.lower().split(','):
                l = l.strip()
                if l:
                    sys.stdout.write('LANG\t' + l + '\t1\n')
