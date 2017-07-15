#!/bin/python3

# Longest Common Subsequence

import sys

s1 = "abcdqf"
s2 = "acbcdf"

N1 = len(s1)+1
N2 = len(s2)+1

dynamic_table = [[0 for x in range(N2)] for y in range(N1)]

length = -1
ansa_i, ansa_j = 0,0

for i in range(1, N1):
    for j in range(1, N2):
        if s1[i-1] == s2[j-1]:
            dynamic_table[i][j] = dynamic_table[i-1][j-1]+1
            if dynamic_table[i][j] > length:
                length = dynamic_table[i][j]
                ansa_i, ansa_j  = i,j

for d in dynamic_table:
    print(d)

substring_list = []

# Backtrack to find ansa:
while ansa_i > 0 and ansa_j > 0:
    if dynamic_table[ansa_i][ansa_j] == 0:
        break
    
    substring_list.append(s2[ansa_i])
    ansa_i -=1
    ansa_j -=1
print("Substring: ", ''.join(substring_list[::-1]))
print("Length of the Substring: ", length)
