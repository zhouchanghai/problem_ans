#SprinklersArrangement
#x moves and y moves are independent
def solution(X,Y):
    n = len(X)
    m = 1000000007
    xcount, ycount = [0]*n, [0]*n
    for x in X:
        xcount[x-1] += 1
    for y in Y:
        ycount[y-1] += 1
    result = 0
    for i, x in enumerate(iterNonEmpty(xcount)):
        result = (result + abs(i-x)) % m
    for i, y in enumerate(iterNonEmpty(ycount)):
        result = (result + abs(i-y)) % m
    return result

def iterNonEmpty(count):
    i = 0
    while i < len(count):
        if count[i] == 0:
            i += 1
        else:
            count[i] -= 1
            yield i
            
print(solution([1, 2, 2, 3, 4], [1, 1, 4, 5, 4]))
print(solution([1, 1, 1, 1], [1, 2, 3, 4]))
print(solution([1, 1, 2], [1, 2, 1]))
