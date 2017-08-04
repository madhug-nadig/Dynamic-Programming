#!/bin/python3

# Minimum Jumps to Reach end

ip = "axwbuicqsdbqeaf"
N = len(ip)
table = [1] * N
maxi = 0
 
for i in range(1, N):
    for j in range(i):
        if ip[i] > ip[j] and (table[i] < table[j] +1):
            table[i] = table[j]+1

ansa = max(table)
last = table.index(ansa)
string = [""]

print(table)
print("Length of longest increasing subsequence: ", ansa)

for i in range(last):
    if ip[i] < ip[last] and ip[i] > string[len(string)-1]:
        string.append(ip[i])

string.append(ip[last])

print(''.join(string))