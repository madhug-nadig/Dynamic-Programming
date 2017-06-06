S = [1,2,3]
n = 5

def count(S, m, n):
    if n == 0 :
        return 1
    if n < 0:
        return 0
    if m<=0 and n >=1:
        return 0
    
    return count(S, m-1, n) + count(S, m, n-S[m-1])

print(count(S, len(S), n))