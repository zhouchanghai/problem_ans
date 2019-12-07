#MaxNotPresent

'''
See these links for explanation
https://stackoverflow.com/questions/52100461
https://blog.csdn.net/kidgin7439/article/details/81535229

Draw an edge between the number A[i] and B[i]). 
This will create a number of disjoint sub-graphs.
There are two types of sub-graphs:
1) Has cycles inside:
Every node can face up. For example (2-3, 3-4, 4-2, 3-5) or (2-2, 2-3)
2) No cycle (a tree):
All nodes except one can face up. Let's discard the largest value.
'''

def solution(A, B):
    n = len(A)
    uf = UnionFind(n+1)
    for a, b in zip(A,B):
        if a>n and b>n: continue
        if a>n:
            a = b
        if b>n:
            b = a
        uf.union(a, b)
    result = n+1
    for i in range(1,n+1):
        root = uf.find(i)
        if uf.circle[root]:
            continue
        else:
            result = min(result, uf.maxVal[root])
    return result
        
class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        #is there a circle in each group
        self.circle = [0]*size
        #max value in each group
        self.maxVal = [i for i in range(size)]
    
    def find(self, val):
        if self.parent[val] == val:
            return val
        self.parent[val] = self.find(self.parent[val])
        return self.parent[val]
        
    def union(self, a, b):
        r1 = self.find(a)
        r2 = self.find(b)
        if r1 == r2:
            self.circle[r1] = 1
        else:
            self.parent[r1] = r2
            self.circle[r2] |= self.circle[r1]
            self.maxVal[r2] = max(self.maxVal[r1], self.maxVal[r2])
            
print(solution([1, 2, 4, 3], [1, 3, 2, 3]))
print(solution([4, 2, 1, 6, 5], [3, 2, 1, 7, 7]))
print(solution([2, 3],[2,3]))
