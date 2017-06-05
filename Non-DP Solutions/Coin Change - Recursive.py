m = [1,2,3,4]
n = 21

def count(S, m, n):
    if n == 0 :
        return 1
    if n < 0:
        return 0
    if m<=0 and n >=1:
        return 0
    
    return count(S, m-1, n) + count(S, m, n-S[n-1])
    