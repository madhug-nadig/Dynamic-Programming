values = [9,8,7,6,5]
weights = [1,2,3,4,5]

def knap(w, v , k):
    N = len(w)
    table = [None] * N
    for i in range(N):
        table[i] = [None] * k
    
    for i in range(N):
        table[i][0] = 0
    
    for i in range(N):
        for j in range(1, k):
            total_weight = j
            if w[i] <= total_weight:
                table[i][j] = w[i]

    print(table)
    return table[N-1][k-1]
    
print(knap(weights, values, 10))
