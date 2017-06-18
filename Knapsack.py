

values = [1,2,3]
weights = [1,2,3]

#start the DP algorithm
def knap(w, v , k):

    N = len(w)

    #Initialize the 2D array
    table = [None] * N
    for i in range(N):
        table[i] = [None] * (k+1)
    #The 0th column, 0 by default since you can't add any item when the max weight is 0
    for i in range(N):
        table[i][0] = 0
    
    # First row init excluding the 0th element
    for j in range(1, k+1):
        if w[0] <= j:
            table[0][j] = w[0]
        else:
            table[0][j] = 0

    # Construct the dynamic table
    for i in range(1, N):
        for j in range(1, k+1):
            total_weight = j
            if w[i] > j:
                table[i][j] = table[i-1][j]
            else:
                #Actual DP happens here. Either you choose the the value right above the current element, or take the 'i'th item 
                table[i][j] = max( table[i-1][j], v[i] + table[i-1][j-w[i]])

    print(table)
    return table[N-1][k]
    
print(knap(weights, values, 6))
