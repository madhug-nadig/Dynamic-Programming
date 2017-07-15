#!/bin/python3

# Longest Common Subsequence

import sys

s1 = "abcdcf"
s2 = "acbcf"

N1 =len(s1)+1
N2 =len(s2)+1

dyna = [[0 for x in range(N2)] for y in range(N1)]

for i in range(1, N1):
    for j in range(1, N2):

        if s2[j-1] == s1[i-1]:
            dyna[i][j] = dyna[i-1][j-1]+1
        else:
            dyna[i][j] = max(dyna[i-1][j], dyna[i][j-1])

for i in dyna:
    print(i)

print("Answer: ", dyna[N1-1][N2-1])