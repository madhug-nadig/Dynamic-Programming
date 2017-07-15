#!/bin/python3

# Minimum Cost Path

import sys

ip = [
            [1,3,5,8],
            [4,2,1,7],
            [4,3,2,3]
        ]

N = len(ip)
M = len(ip[0])

#copy into a dynamic array
dyna = [[ip[y][x] for x in range(M)] for y in range(N)]

for i in range(N):
    for j in range(M):
        if (i ==0 and j ==0):
            continue
        if i == 0:
            dyna[i][j] += dyna[i][j-1]
        elif j == 0:
            dyna[i][j] += dyna[i-1][j]
        else:
            dyna[i][j] += min(dyna[i-1][j], dyna[i][j-1])

for i in dyna:
    print(i)
print("Minimum Cost:", dyna[N-1][M-1])
