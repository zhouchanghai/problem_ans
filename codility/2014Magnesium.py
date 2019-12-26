# AscendingPaths (Hard, Ambitious)
# https://app.codility.com/programmers/task/ascending_paths/
# 1987 started, 99 silver, 127 golden
# 100% O(N + M * logM) https://app.codility.com/demo/results/trainingQZ3ABR-TCN/
# Official solution https://codility.com/media/train/solution-ascending-paths.pdf

def solution(N,A,B,C):
    if not A:
        return 0
    dist = list(zip(C,A,B))
    dist.sort()
    # dp[i] is the longest path ends at i
    dp = [0]*N
    curDist = dist[0][0]
    update = {}
    for i, t in enumerate(dist):
        d, a, b = t
        if d != curDist:
            for node, path in update.items():
                dp[node] = path
            curDist = d
            update.clear()
        # a -> b
        update[b] = max(update.get(b, dp[b]), dp[a] + 1)
        # b -> a
        update[a] = max(update.get(a, dp[a]), dp[b] + 1)

    for node, path in update.items():
        dp[node] = path
    return max(dp)
    

A=[0,1,1,2,3,4,5,3]
B=[1,2,3,3,4,5,0,2]
C=[4,3,2,5,6,6,8,7]
print(solution(6,A,B,C)) # 4
print(solution(1,[],[],[])) # 0
print(solution(1,[0],[0],[1])) # 1
print(solution(2,[0,0,0,0],[1,1,1,1],[1,2,3,4])) # 4
print(solution(1,[0,0,0,0],[0,0,0,0],[1,2,3,4])) # 4
