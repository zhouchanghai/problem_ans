# MaxDistanceMonotonic (Hard, Ambitious)
# Find a pair (P, Q), such that A[P] <= A[Q] and the value Q - P is maximal.
# https://app.codility.com/programmers/task/max_distance_monotonic/
# 6301 started, 1696 silver, 394 golden
# This O(N logN) solution is not optimal.
# See the official solution of O(N) at
# https://codility.com/media/train/solution-max-distance-monotonic.pdf

def solution(A):
    desc = []
    result = 0
    for i, x in enumerate(A):
        if not desc or x < desc[-1][0]:
            desc.append((x,i))
        else:
            result = max(result, i - firstLessEqual(desc, x))
    return result

def firstLessEqual(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid][0] <= x:
            hi = mid
        else:
            lo = mid + 1
    return a[lo][1]
    
print(solution([5,3,6,3,4,2])) # 3
print(solution([1,1,1,1])) # 3
