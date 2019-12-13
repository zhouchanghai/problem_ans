#NumberOfDiscIntersections (Medium)
#100% O(N * logN) https://app.codility.com/demo/results/trainingUQH7Q7-TH7/
def solution(A):
    left = []
    for i, r in enumerate(A):
        left.append((i-r,i))
    left.sort()
    
    result = 0
    #Note: queue.PriorityQueue() only got 81% score
    #See https://app.codility.com/demo/results/trainingDSKSQM-JSY/
    active = MinHeap(len(A))
    for x, i in left:
        while active.size:
            if active.q[1] < x:
                active.pop()
            else:
                break
        result += active.size
        if result > 10000000:
            return -1
        active.put(i+i-x)
    return result

class MinHeap:
    def __init__(self,n):
        self.q = [None]*(n+1)
        self.size = 0
    
    def put(self, key):
        self.size += 1
        self.q[self.size] = key
        self.swim(self.size)

    def pop(self):
        self.q[1] = self.q[self.size]
        self.q[self.size] = None
        self.size -= 1
        self.sink(1)

    def swim(self, k):
        q = self.q
        while (k > 1 and q[k//2] > q[k]):
            up = k//2
            q[up], q[k] = q[k], q[up]
            k = up

    def sink(self, k):
        q = self.q
        while (2*k <= self.size):
            j = 2*k;
            if j < self.size and q[j] > q[j+1]: j += 1
            if q[k] <= q[j]: break
            q[k], q[j] = q[j], q[k]
            k = j


print(solution([1,5,2,1,4,0]))
