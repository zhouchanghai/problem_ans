from itertools import accumulate

#https://app.codility.com/programmers/challenges/ferrum2018/
def solution(A):
    if not A: return 0
    acc = list(accumulate(A))
    ret = 1 if A[0] >= 0 else 0
    idx = [0] #sum(A[idx[0] .. i]) < sum(A[idx[1] .. i]) < ... < sum(A[idx[-1] .. i]) 
    for i in range(1, len(A)):
        if getSum(acc, idx[-1], i) < A[i]:
            idx.append(i)
        
        #assert sum(A[idx[lo] .. i]) < 0 and sum(A[idx[hi] .. i]) >= 0 
        lo, hi = -1, len(idx)
        while lo+1 < hi:
            mid = (hi+lo) >> 1
            if getSum(acc, idx[mid], i) >= 0:
                hi = mid
            else:
                lo = mid
        if hi < len(idx) and i-idx[hi]+1 > ret:
            ret = i-idx[hi]+1
    return ret

def getSum(acc,i,j):
    return acc[j] if i==0 else acc[j] - acc[i-1]

def bruteForce(A):
    acc = list(accumulate(A))
    n = len(A)
    ret = 0
    for i in range(n):
        for j in range(i,n):
            if getSum(acc, i, j) >= 0 and j-i+1 > ret:
                ret = j-i+1
    return ret
    

if __name__ == "__main__":
    import random
    def test(n):
        a = [random.randint(-1,1) for i in range(n)]
        s = solution(a)
        b = bruteForce(a)
        print(a, s, b)
        assert s == b

    for i in range(100):
        test(5)
        
    print(solution([-1, -1, 1, -1, 1, 0, 1, -1, -1])) #7
    print(solution([1, 1, -1, -1, -1, -1, -1, 1, 1])) #4
