# TripPlanning (Hard, Ambitious)
# https://app.codility.com/programmers/task/trip_planning/
# 4584 started, 243 silver, 118 golden
# 100% O(N logN) https://app.codility.com/demo/results/trainingQUPPDS-29M/

import collections, queue

class Node:
    def __init__(self, id):
        self.id = id
        self.children = []

def solution(K, T):
    n = len(T)
    if n == 1:
        return [0]

    adj = [[] for i in range(n)]
    for a, b in enumerate(T):
        if a == b: continue
        adj[a].append(b)
        adj[b].append(a)
    
    # build the tree rooted at K
    nodes = [Node(i) for i in range(n)]
    q = collections.deque([K])
    visited = [0]*n
    while q:
        i = q.popleft()
        visited[i] = 1
        for j in adj[i]:
            if not visited[j]:
                nodes[i].children.append(nodes[j])
                q.append(j)
    
    # Find deepest leaf for every node
    # Note: the recursive version may cause stack overflow for large input
    findDeepestNonRecursive(nodes[K])

    # Cut the tree into forest along the longest path
    result = [K]
    q = queue.PriorityQueue()
    q.put((-nodes[K].cities, nodes[K].target, K))
    while q.qsize() > 0:
        c, target, i = q.get()
        result.append(target)
        splitTree(nodes[i], target, q)
        
    return result
        
def splitTree(root, target, q):
    while root:
        if root.id == target:
            return
        for child in root.children:
            if child.target != target:
                q.put((-child.cities, child.target, child.id))
            else:
                nextRoot = child
        root = nextRoot

def findDeepest(root):
    if not root.children:
        root.target = root.id
        root.cities = 1
        return

    target, cities = None, 0
    for child in root.children:
        findDeepest(child)
        if ((child.cities > cities) or 
            (child.cities == cities and child.target < target)):
            target, cities = child.target, child.cities
    root.target = target
    root.cities = cities + 1
    
def findDeepestNonRecursive(root):
    callStack = [root]
    resultStack = []
    while callStack:
        root = callStack.pop()
        resultStack.append(root)
        if not root.children:
            root.target = root.id
            root.cities = 1
        else:
            root.cities = 0
            for child in root.children:
                callStack.append(child)

    for node in reversed(resultStack):
        if node.cities > 0:
            continue
        target, cities = None, 0
        for child in node.children:
            if ((child.cities > cities) or 
                (child.cities == cities and child.target < target)):
                target, cities = child.target, child.cities
        node.target = target
        node.cities = cities + 1


print(solution(2, [1,2,3,3,2,1,4]))
print(solution(0, [0]))
