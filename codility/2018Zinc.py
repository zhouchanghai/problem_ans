#TheaterTickets

def solution(A):
    n = len(A)
    if n < 3: return 0
    
    visited = [0]*(n+1)
    #distinct numbers in A[0 ... i]
    singles = [0]*n
    singles[0] = 1
    visited[A[0]] = 1
    for i in range(1,n):
        if visited[A[i]]:
            singles[i] = singles[i-1] 
        else:
            singles[i] = singles[i-1] + 1
            visited[A[i]] = 1

    pairs = getTuples(A, singles, 2)
    triples = getTuples(A, pairs, 3)
    return triples[-1] % 1000000007

# Given m-tuples, output (m+1)-tuples.
# tuples[i]: distinct m-tuples in A[0 ... i]
def getTuples(A, tuples, newSize):
    n = len(A)
    result = [0]*n
    # pos[i] is the previous position of A[i]
    pos = [-1]*(n+1)
    
    # count of new size tuples end at i is tuple[i-1]
    for i in range(newSize-1, n):
        num = A[i]
        if pos[num] < 0:
            result[i] = result[i-1] + tuples[i-1]
        else:
            result[i] = result[i-1] + tuples[i-1] - tuples[pos[num] - 1]
        pos[num] = i
    return result

print(solution([1, 1, 1, 1, 1]))
print(solution([1, 2, 1, 1]))
print(solution([1, 2, 3, 4]))
print(solution([2, 2, 2, 2]))
print(solution([2, 2, 1, 2, 2]))
print(solution([1,2]))
