def solve(a, b):
    if a==b:
        return 0
    steps = [[-1]*8 for i in range(8)]
    r0,c0 = ord(a[1])-ord('1'), ord(a[0])-ord('a')
    r1,c1 = ord(b[1])-ord('1'), ord(b[0])-ord('a')

    steps[r0][c0] = 0
    q = [(r0,c0)]
    moveR = [1,1,-1,-1,2,2,-2,-2]
    moveC = [2,-2,2,-2,1,-1,1,-1]
    while q:
        tmp = set()
        for r,c in q:
            for m in range(8):
                newR = r+moveR[m]
                newC = c+moveC[m]
                if newR >= 8 or newR < 0 or newC >=8 or newC < 0:
                    continue
                if steps[newR][newC] >=0: #visited
                    continue
                steps[newR][newC] = steps[r][c] + 1
                if (newR, newC) == (r1,c1):
                    return steps[newR][newC]
                tmp.add((newR, newC))
        q = tmp

try:
    while True:
        line = input()
        if not line: break
        a, b = line.strip().split()
        print("To get from {} to {} takes {} knight moves.".format(a,b,solve(a,b)))
except EOFError:
    pass
