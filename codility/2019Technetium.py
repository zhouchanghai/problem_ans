def solution(A):
    rows, cols = len(A), len(A[0])
    result = [A[0][0]]
    dp = [(0,0)]
    for i in range(rows+cols-2):
        candidate = 0
        for x,y in dp:
            #go down
            if x+1 < rows and A[x+1][y] > candidate:
                candidate = A[x+1][y]
            #go right
            if y+1 < cols and A[x][y+1] > candidate:
                candidate = A[x][y+1]
        result.append(candidate)
        tmp = set()
        for x,y in dp:
            if x+1 < rows and A[x+1][y] == candidate:
                tmp.add((x+1,y))
            if y+1 < cols and A[x][y+1] == candidate:
                tmp.add((x,y+1))
        dp = tmp
    return "".join(str(d) for d in result)
    
print(solution([[9,9,7],[9,7,2],[6,9,5,], [9,1,2]]))
print(solution([[9,9,9],[9,9,9],[9,9,9,]]))
