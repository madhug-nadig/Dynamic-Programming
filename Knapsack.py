values = [1,4,5,7]
weights = [1,3,4,5]

def knap(w, v , k):
    N = len(w)
    table = [None] * N
    for i in range(N):
        table[i] = [None] * (k+1)
    
    for i in range(N):
        table[i][0] = 0
    
    for j in range(1, k+1):
        if w[0] <= j:
            table[0][j] = w[0]
        else:
            table[0][j] = 0

    for i in range(1, N):
        for j in range(1, k+1):
            total_weight = j
            if w[i] > j:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = max( table[i-1][j], v[i] + table[i-1][j-w[i]])

    print(table)
    return table[N-1][k]
    
print(knap(weights, values, 7))
