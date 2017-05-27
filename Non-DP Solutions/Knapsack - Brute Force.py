value = [9,8,7,6,5]
weights = [1,2,3,4,5]

def powerset(items):
    #Empty elements already present
    res = [[]]
    for item in items:
        newset = [r+ [item] for r in res]
        res.extend(newset)
    return res

def knap(p, k):
    knap = []
    optimal_wt = 0
    optimal_vl = 0
    for st in p:
        wt = sum([x[0] for x in st])
        vl = sum([x[1] for x in st])

        if vl > optimal_vl and wt <= k:
            optimal_vl = vl
            optimal_wt = wt
            knap = st
    return knap

p = powerset(zip(value, weights))

print(p, len(p))
print(knap(p, 10))
