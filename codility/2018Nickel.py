#PascalTriangle (Medium)
def solution(P):
    segments = []
    start = 0
    for i, v in enumerate(P):
        if v != P[start]:
            segments.append((P[start], i-start))
            start = i
    segments.append((P[start], len(P)-start))
    result = 0
    while len(segments) > 1:
        tmp = []
        for i in range(len(segments)):
            v, size = segments[i]
            if v:
                result += size
                size -= 1
                if i > 0:
                    size += 1
                if i < len(segments) - 1:
                    size += 1
                if tmp and tmp[-1][0]:
                    tmp[-1] = (tmp[-1][0], tmp[-1][1]+size)
                else:
                    tmp.append((v,size))
            else:
                size -= 1
                if size > 0:
                    tmp.append((v,size))
        segments = tmp
    
    v, size = segments[0]
    if v:
        result += size * (size+1) // 2
    limit = 1000000000
    return limit if result > limit else result

print(solution([True, False, False, True, False]))
print(solution([1,0,0,1]))
print(solution([0,0,0]))
print(solution([1,1,1]))
