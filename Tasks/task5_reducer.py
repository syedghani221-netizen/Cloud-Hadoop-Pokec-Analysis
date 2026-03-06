#!/usr/bin/env python3
import sys
import math
current_key = None
users = []
def cosine_sim(a, b):
    if a == 0 or b == 0:
        return 0.0
    return (a*b)/(math.sqrt(a**2)*math.sqrt(b**2))
for line in sys.stdin:
    parts = line.strip().split('\t')
    if len(parts) != 2:
        continue
    key = parts[0]
    uid, comp = parts[1].split(',')
    if current_key == key:
        users.append((uid, float(comp)))
    else:
        if current_key and len(users) >= 2:
            best_sim = -1
            best_pair = None
            for i in range(len(users)):
                for j in range(i+1, len(users)):
                    s = cosine_sim(users[i][1], users[j][1])
                    if s > best_sim:
                        best_sim = s
                        best_pair = (users[i][0], users[j][0])
            if best_pair:
                sys.stdout.write('Group:' + current_key + ' | Users:' + best_pair[0] + '&' + best_pair[1] + ' | Sim:' + str(round(best_sim,4)) + '\n')
        current_key = key
        users = [(uid, float(comp))]
