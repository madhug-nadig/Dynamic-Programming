#!/bin/python3

# Maximum Sum Increasing Subsequence

ip = [1,2,3,4,100,33,44,12,109]
N = len(ip)
table = [x for x in ip]


for i in range(1, N):
    for j in range(i):
        if ip[i] > ip[j] and (table[i] < table[j] + ip[i]):
            table[i] = table[j]+ ip[i]

ansa = max(table)
last = table.index(ansa)


print(table)
print("Length of longest increasing subsequence: ", ansa)

