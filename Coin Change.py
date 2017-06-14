dynamic_table = [[0 for i in range(m)] for i in range(n+1)]
    #print(dynamic_table)
for i in range(m):
    #print(dynamic_table[0][i])
    dynamic_table[0][i] = 1
for i in range(1, n+1):
    for j in range(m):
       dynamic_table[i][j] = (dynamic_table[i - S[j]][j] if i-S[j] >= 0 else 0) + (dynamic_table[i][j-1] if j >= 1 else 0)
return dynamic_table[n][m-1]