# ReplacingBooks (Medium, Respectable)
# https://app.codility.com/programmers/task/replacing_books/
# 3021 started, 41 silver, 125 golden

class MaxCountHeap:
    def __init__(self,n):
        self.q = [None]*(n+1) #(count, key) pairs
        self.size = 0 #size of the heap
        self.pos = {} #position of a key in q
        
    def maxCount(self):
        return self.q[1][0]
    
    def increase(self, key, num=1):
        if key not in self.pos:
            self.size += 1
            self.q[self.size] = (num, key)
            self.pos[key] = self.size
            self.swim(self.size)
        else:
            pos = self.pos[key]
            count, key = self.q[pos]
            self.q[pos] = (count+num, key)
            self.swim(pos)
            
    def decrease(self, key, num=1):
        pos = self.pos[key]
        count, key = self.q[pos]
        self.q[pos] = (count-num, key)
        self.sink(pos)
        
    def swim(self, k):
        q, pos = self.q, self.pos
        while (k > 1 and q[k//2] < q[k]):
            up = k//2
            q[up], q[k] = q[k], q[up]
            pos[q[up][1]] = up
            pos[q[k][1]] = k
            k = up

    def sink(self, k):
        q, pos = self.q, self.pos
        while (2*k <= self.size):
            j = 2*k;
            if j < self.size and q[j] < q[j+1]: j += 1
            if q[k] >= q[j]: break
            q[k], q[j] = q[j], q[k]
            pos[q[k][1]] = k
            pos[q[j][1]] = j
            k = j
            
            
def solution(A, K):
    if K >= len(A) - 1:
        return len(A)

    result = K + 1;
    h = MaxCountHeap(len(A))
    h.increase(A[0]);
    left, right = 0, 1 #[left, right)
    while right < len(A):
        if h.maxCount() + K >= right - left:
            result = max(result, right - left)
            h.increase(A[right])
            right += 1
        else:
            h.decrease(A[left])
            left += 1

    if h.maxCount() + K >= right - left:
        result = max(result, right - left)
    return result

print(solution([1, 1, 3, 4, 3, 3, 4], 2))
print(solution([4, 5, 5, 4, 2, 2, 4], 0))
print(solution([1, 3, 3, 2], 3))
print(solution([0, 0, 1, 1, 1], 0))
print(solution([0, 0, 1, 1, 1], 1))
