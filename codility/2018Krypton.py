def solution(A):
    n = len(A)
    hasZero = any(x==0 for row in A for x in row)
    previous = None
    for row in A:
        if not previous:
            previous = []
            for x in row:
                c2 = getCount(x,2)
                c5 = getCount(x,5)
                if not previous:
                    previous.append((c2,c5))
                else:
                    left2, left5 = previous[-1]
                    previous.append((c2 + left2, c5 + left5))
            continue
        
        current = []
        for i, x in enumerate(row):
            up = previous[i]
            c2 = getCount(x,2)
            c5 = getCount(x,5)
            if i == 0:
                current.append((c2+up[0], c5+up[1]))
            else:
                left = current[-1]
                c2 += min(left[0], up[0])
                c5 += min(left[1], up[1])
                current.append((c2,c5))
        previous = current
        
    result = min(previous[-1])
    if hasZero:
        result = min(1, result)
    return result
        
def getCount(x, p):
    if x == 0:
        return 1
    rt = 0
    while x%p == 0:
        rt += 1
        x //= p
    return rt
    
    
print(solution([[2,10,1,3],[10,5,4,5],[2,10,2,1],[25,2,5,1]]))
print(solution([[10,1,10,1],[1,1,1,10],[10,1,10,1],[1,10,1,1]]))
print(solution([[10,10,10],[10,0,10],[10,10,10]]))
