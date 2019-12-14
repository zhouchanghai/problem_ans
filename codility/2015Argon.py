# TrekAndSwim (Hard, Ambitious)
# https://app.codility.com/programmers/task/trek_and_swim/
# 2588 started, 151 silver, 172 golden
# O(N) https://app.codility.com/demo/results/trainingRX9YMH-3E8/

def solution(A):
    n = len(A)
    left = leader0Size(A)
    right = leader0Size([1-x for x in reversed(A)])
    right.reverse()
    result = 0
    for i in range(n-1):
        sizeL = left[i]
        sizeR = right[i+1]
        if sizeL > 0 and sizeR > 0:
            result = max(result, sizeL + sizeR)
    return result

def leader0Size(a):
    # replace 0 with -1
    # sumPos[i] is the first position that sum(a[0 ... pos]) == i
    # if i < j then sumPos[i] < sumPos[j]
    n = len(a)
    sumPos = [None] * (n+2)
    sumPos[0] = -1
    result = [0]*n
    s = 0
    for i, x in enumerate(a):
        if x == 1:
            s += 1
            if s >= 0 and sumPos[s] is None:
                sumPos[s] = i
        else:
            s -= 1
        if s < 0:
            result[i] = i+1
        elif sumPos[s+1] is not None:
            result[i] = i - sumPos[s+1]
    return result

print(solution([1,1])) #0
print(solution([0,0])) #0
print(solution([1,0])) #0
print(solution([0,1])) #2
print(solution([1,1,0,1,0,0,1,1])) #7
