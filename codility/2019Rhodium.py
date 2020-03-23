# TreeRange (Medium, Respectable)
# https://app.codility.com/programmers/task/tree_range/
# 4126 started, 158 silver, 105 golden
# 100% O(N * N) https://app.codility.com/cert/view/certW6F6WA-XTSVEEBV8CMPMSN2/details/

import collections
def solution(T):
    n = len(T)
    adj = [[] for i in range(n)]
    for i in range(n):
        if T[i] != i:
            adj[i].append(T[i])
            adj[T[i]].append(i)
    # minMax[i] is the min and max value in the path from i to i+1
    minMax = [getMinMax(adj, i) for i in range(n-1)]
    result = n
    for start in range(n):
        lower, upper = start, start
        for end in range(start+1, n):
            if minMax[end-1][0] < lower:
                break
            upper = max(upper, minMax[end-1][1])
            if upper == end:
                result += 1
    return result

def getMinMax(adj, start):
    n = len(adj)
    result = (start, start+1)
    parent = [None] * n
    q = collections.deque()
    q.append(start)
    while q:
        i = q.popleft()
        if i == start + 1:
            break
        for j in adj[i]:
            if j != parent[i]:
                q.append(j)
                parent[j] = i
    lower, upper = start, start + 1
    i = start + 1
    while i is not None:
        lower = min(lower, i)
        upper = max(upper, i)
        i = parent[i]
    return lower, upper

