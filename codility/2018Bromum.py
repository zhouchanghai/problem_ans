from collections import Counter
def solution(N, Q, B, C):
    buckets = [None]*N
    for i in range(len(B)):
        b,c = B[i], C[i]
        if buckets[b] is None:
            buckets[b] = Counter()
        buckets[b][c] += 1
        if buckets[b][c] == Q:
            return i
    return -1
