# BreakTheRope (Hard, Ambitious)
# https://app.codility.com/programmers/task/break_the_rope/
# 5943 started, 908 silver, 193 golden
# 100% O(N * logN) https://app.codility.com/demo/results/trainingDNY7UA-RPW/

def solution(A, B, C):
    n = len(A)
    root = Node(-1, 900000000, 0)
    nodes = [None]*n
    for i in range(n):
        nodes[i] = Node(i, A[i], B[i])
        if C[i] < 0:
            root.addChild(nodes[i])
        else:
            nodes[C[i]].addChild(nodes[i])
            
    lo, hi = -1, n-1
    while lo < hi:
        mid = (lo + hi + 1)//2
        # The recursive version will cause stack overflow for large n
        if sumWeightsNonRecursive(root, mid) < 0:
            hi = mid - 1
        else:
            lo = mid
    return lo + 1

# sum of weights for nodes <= i
# return -1 if any rope breaks
def sumWeights(root, i):
    if (not root) or root.i > i :
        return 0
    if root.weight > root.durability:
        return -1
    s = root.weight
    if root.children:
        for child in root.children:
            w = sumWeights(child, i)
            if w < 0:
                return -1
            s += w
    if s > root.durability:
        return -1
    return s

# https://algorithms.tutorialhorizon.com/binary-tree-postorder-traversal-non-recursive-approach/
def sumWeightsNonRecursive(root, i):
    if (not root) or root.i > i :
        return 0
    stack1 = [root]
    stack2 = []
    while stack1:
        head = stack1.pop()
        if head.weight > head.durability:
            return -1
        stack2.append(head)
        isLeaf = True
        if head.children:
            for child in head.children:
                if child.i <= i:
                    stack1.append(child)
                    isLeaf = False
                else:
                    child.sum = 0
        if isLeaf:
            head.sum = head.weight
        else:
            head.sum = -1
    for node in reversed(stack2):
        if node.sum < 0:
            node.sum = node.weight
            for child in node.children:
                node.sum += child.sum
            if node.sum > node.durability:
                return -1
    return stack2[0].sum
    
class Node:
    def __init__(self, i, durability, weight):
        self.i = i
        self.durability  = durability
        self.weight = weight
        self.children = None
        
    def addChild(self, child):
        if self.children is None:
            self.children = []
        self.children.append(child)
        
print(solution([1], [2], [-1]))
print(solution([5,3,6,3,3], [2,3,1,1,2], [-1,0,-1,0,3]))
print(solution([4,3,1], [2,2,1], [-1,0,1]))
