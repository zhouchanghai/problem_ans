def solution(A, B):
    if sum(A) != sum(B):
        return -1
    n = len(A)
    if n==1: return 0
    result = 0
    m = 1000000007
    pre,cur = 0, A[0]-B[0]
    for i in range(1,n):
        #move pre stones between i and i-2
        result = (result + abs(pre))%m
        pre, cur = cur, pre + A[i]-B[i]
        if (pre>0 and cur<0) or (pre<0 and cur>0):
            if abs(pre) > abs(cur):
                result = (result + abs(cur))%m
                pre, cur = pre+cur, 0
            else:
                result = (result + abs(pre))%m
                pre,cur = 0, pre+cur
    return result

print(solution( [1, 1, 2, 4, 3], [2, 2, 2, 3, 2]))
print(solution([0, 0, 2, 1, 8, 8, 2, 0], [8, 5, 2, 4, 0, 0, 0, 2]))
print(solution([10**9, 10**9, 10**9, 0, 0, 0],  [0, 0, 0, 10**9, 10**9, 10**9]))
print(solution([2],[1] ))
