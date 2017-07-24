#!/bin/python3

# Minimum Jumps to Reach end

arr = [2,3,1,1,2,4,2,0,1,1]
N = len(arr)
jumps = [10000] * N
jumps[0] = 0
 
for i in range(1, N):
    for j in range(i):
        if i <= j + arr[j]:
            jumps[i] = min(jumps[i], jumps[j] + 1)
           
print(jumps)
print("Min number of jumps: ", jumps[N-1])