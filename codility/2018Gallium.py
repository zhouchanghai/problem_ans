from collections import Counter

# MaxZeroProduct

# 2**30 > 10**9 and 5**13 > 10**9
# So the (2**x, 5**y) factors are limited.
def solution(A):
    counter = Counter()
    for n in A:
        p2, p5 = 0, 0
        while n%2 == 0:
            p2 += 1
            n //= 2
        while n%5 == 0:
            p5 += 1
            n //= 5
        counter[(p2,p5)] += 1
    result = 0
    factors = [(k[0], k[1], counter[k]) for k in counter]
    n = len(factors)
    for i in range(n):
        a2, a5, _ = factors[i]
        for j in range(i+1, n):
            b2, b5, _ = factors[j]
            for k in range(j+1, n):
                c2, c5, _ = factors[k]
                result = max(result, min(a2+b2+c2, a5+b5+c5))

    for i in range(n):
        a2, a5, acount = factors[i]
        if acount >= 3:
            result = max(result, 3 * min(a2,a5))
        if acount < 2: continue
        for j in range(n):
            if j == i: continue
            b2, b5, _ = factors[j]
            result = max(result, min(a2+a2+b2, a5+a5+b5))
    return result
    
print(solution([7, 15, 6, 20, 5, 10]))
print(solution([25, 10, 25, 10, 32]))
