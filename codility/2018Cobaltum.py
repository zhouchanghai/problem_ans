#IncreasingSequences (Medium)
def solution(A, B):
    dpSwap = [1]
    dpNoSwap = [0]
    n = len(A)
    for i in range(1, n):
        swap, noSwap = n, n
        possible = 0
        if A[i-1] < A[i] and B[i-1] < B[i]:
            possible = 1
            # i-1 no swap, i no swap
            noSwap = min(noSwap, dpNoSwap[-1])
            # i-1 swap, i swap
            swap = min(swap, dpSwap[-1] + 1)
        if A[i-1] < B[i] and B[i-1] < A[i]:
            possible = 1
            # i-1 no swap, i swap
            swap = min(swap, dpNoSwap[-1] + 1)
            # i-1 swap, i no swap
            noSwap = min(noSwap, dpSwap[-1])
        if not possible:
            return -1
        dpSwap.append(swap)
        dpNoSwap.append(noSwap)
    return min(dpSwap[-1], dpNoSwap[-1])

print(solution([5, 3, 7, 7, 10], [1, 6, 6, 9, 9])) #2
print(solution([5, -3, 6, 4, 8], [2, 6, -5, 1, 0])) #-1
print(solution([1, 5, 6], [-2, 0, 2])) #0
