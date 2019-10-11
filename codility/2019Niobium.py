from collections import Counter
def solution(A):
    c = Counter()
    bits = ["0", "1"]
    for row in A:
        flip1 = "".join(bits[x] for x in row)
        flip0 = "".join(bits[1-x] for x in row)
        c[flip1] += 1
        c[flip0] += 1
    return c.most_common(1)[0][1]

print(solution([[0,0,0,0],[0,1,0,0],[1,0,1,1]]))
print(solution([[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]]))
