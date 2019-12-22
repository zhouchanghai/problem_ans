# MaxSliceSwap (Hard, Ambitious)
# https://app.codility.com/programmers/task/max_slice_swap/
# 2456 started, 117 silver, 58 golden
# 100% O(N) https://app.codility.com/demo/results/trainingPX3TEK-2C2/

def solution(A):
    largest = max(A)
    if largest <= 0:
        return largest

    n = len(A)
    revA = list(reversed(A))
    return max(helper(A), helper(revA))

def helper(A):
    n = len(A)
    # maxR[i] is the max value in A[i:]
    # The extra one is for index of -1
    maxR = [-10000]*(n+1)
    for i in range(n-1, -1, -1):
        maxR[i] = max(A[i], maxR[i+1])

    # left[i] is the max sum of slices end at i without swap
    left = [0]*(n+1)
    for i in range(n):
        if left[i-1] <= 0:
            left[i] = A[i]
        else:
            left[i] = left[i-1] + A[i]

    # prefixSum[i] is sum of A[0 ... i]
    prefixSum = [0]*(n+1)
    for i in range(n):
        prefixSum[i] = prefixSum[i-1] + A[i]

    # For any i, we split A[i ... n-1] to two parts, A[i ...  j] and A[j+1 ... n-1].
    # right[i] is the max value of sum(A[i ... j]) + max(A[j+1 ... n-1])
    # which is the best result if we swap i-1 with some k > i-1
    # Note: the first part can be empty, but the second part can't.
    right = [0]*(n+1)
    # for i=n-1, the first part is empty, the second part is A[n-1]
    right[n-1] = A[n-1]
    pre = prefixSum[n-2] + maxR[n-1]
    for i in range(n-2, -1, -1):
        # split between i-1 and i
        tmp = prefixSum[i-1] + maxR[i]
        pre = max(pre, tmp)
        right[i] = pre - prefixSum[i-1]
    
    result = left[n-1]
    for i in range(n):
        L = left[i-1]
        R = right[i+1]
        result = max(result, L, R, L+R)
        
    """print(A)
    print("maxR", maxR)
    print("left", left)
    print("prefixSum", prefixSum)
    print("right", right)"""
    return result

print(solution([1]))
print(solution([1,1]))
print(solution([1,1,1]))
print(solution([3,2,-6,3,1]))
print(solution([1,2,-4,4,5,2,-1,2]))
