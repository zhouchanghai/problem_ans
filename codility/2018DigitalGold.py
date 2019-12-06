#DividingTheKingdom
def solution(N,M,X,Y):
    golds = len(X)
    if golds % 2:
        return 0
    golds = golds // 2
    rows = [0]*N
    cols = [0]*M
    for x,y in zip(X,Y):
        rows[x] += 1
        cols[y] += 1
    return getDivides(rows, golds) + getDivides(cols, golds)

def getDivides(a, target):
    result = 0
    for i in range(len(a)):
        if i > 0:
            a[i] += a[i-1]
        if a[i] > target:
            break
        if a[i] == target:
            result += 1
    return result
    
print(solution(5, 5, [0, 4, 2, 0], [0, 0, 1, 4]))
