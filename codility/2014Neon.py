# BoatAlignment (Hard, Ambitious)
# https://app.codility.com/programmers/task/boat_alignment/
# 4837 started, 78 silver, 114 golden

# **** Solution 1 ****
# Adapted from http://www.voidcn.com/article/p-rxaskvao-bct.html
# 100% O(N) https://app.codility.com/demo/results/trainingM6X876-BB4/
def solution(R, X, M):
    n = len(R)
    if 2*X*n > M:
        return -1
    maxRight = [0]*n
    # First, push all boats to the left and calculate the largest
    # "right" distance which means how right the boat is from its bollard.
    for i in range(n-1, -1, -1):
        center = i*2*X + X
        maxRight[i] = center - R[i]
        if i != n-1:
            maxRight[i] = max(maxRight[i], maxRight[i+1])

    # Then push the boats to the right to reduce "left" distance
    result, move = 0, 0
    for i in range(n):
        center = i*2*X + X + move
        leftDist = R[i] - center
        rightDist = maxRight[i] + move
        diff = leftDist - rightDist
        if diff > 1:
            move += min(diff//2, M - 2*n*X - move)
        center = i*2*X + X + move
        result = max(result, abs(center - R[i]))
    return result

# **** Solution 2 ****
# Binary search for the largest distance.
# 86% O(N log(2 * X * N)) https://app.codility.com/demo/results/trainingZ5R4E2-AZZ/
def solutionSilver(R, X, M):
    n = len(R)
    if 2*X*n > M:
        return -1
    lo, hi = 0, 2*X*n
    while lo < hi:
        mid = (lo+hi)//2
        if isPossible(R, X, M, mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
        
def isPossible(R, X, M, L):
    preRight = 0
    for r in R:
        center = max(preRight+X, r-L)
        right = center + X
        if right > M or abs(r - center) > L:
            return False
        preRight = right
    return True

import random
def test():
    X = 2
    M = 20
    R = [random.randint(0,M) for i in range(3)]
    R.sort()
    s1 = solution(R,X,M)
    s2 = solutionSilver(R,X,M)
    print(R, s1, s2)
    assert s1 == s2

print(solution([1,3,14], 2, 16))
for i in range(10):
    test()
