class MaxHeap:
    def __init__(self,n):
        self.q = [None]*(n+1)
        self.count = 0
        self.pos = {}
    
    def insert(self, c, v):
        self.count += 1
        self.q[self.count] = (c,v)
        self.pos[v] = self.count
        self.swim(self.count)
        
    def increase(self, val):
        if val not in self.pos:
            self.insert(1, val)
        else:
            pos = self.pos[val]
            count, val = self.q[pos]
            self.q[pos] = (count+1, val)
            self.swim(pos)
            
    def decrease(self, val):
        pos = self.pos[val]
        count, val = self.q[pos]
        self.q[pos] = (count-1, val)
        self.sink(pos)
        
    def swim(self, k):
        q = self.q
        pos = self.pos
        while (k > 1 and q[k//2] < q[k]):
            up = k//2
            q[up], q[k] = q[k], q[up]
            pos[q[up][1]] = up
            pos[q[k][1]] = k
            k = up

    def sink(self, k):
        q = self.q
        pos = self.pos
        while (2*k <= self.count):
            j = 2*k;
            if j < self.count and q[j] < q[j+1]: j += 1
            if q[k] >= q[j]: break
            q[k], q[j] = q[j], q[k]
            pos[q[k][1]] = k
            pos[q[j][1]] = j
            k = j
            
            
def solution(K, M, A):
    minCount = len(A)//2
    for i in range(K):
        A[i] += 1
    d = {}
    for x in A:
        d[x] = d.get(x,0) + 1
    h = MaxHeap(len(A)*2)
    ret = set()
    for val,count in d.items():
        h.insert(count,val)
    count, val = h.q[1]
    if count > minCount:
        ret.add(val)
    
    for i in range(K, len(A)):
        #change A[i-K] to A[i-K]-1
        h.decrease(A[i-K])
        A[i-K] -= 1
        h.increase(A[i-K])
        #change A[i] to A[i]+1 
        h.decrease(A[i])
        A[i] += 1
        h.increase(A[i])
        
        count, val = h.q[1]
        if count > minCount:
            ret.add(val)
    ret = list(ret)
    ret.sort()
    return ret

print(solution(3,5,[2,1,3,1,2,2,3]))
print(solution(4,2,[1,2,2,1,2]))
print(solution(5,2,[1,2,2,1,2]))
a= [i*2 for i in range(100000)]
print(solution(50000,100000,a))
