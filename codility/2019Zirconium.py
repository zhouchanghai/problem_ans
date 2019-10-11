def solution(A, B, F):
    ret = sum(B)
    gain = [a-b for a,b in zip(A,B)]
    gain.sort(reverse=True)
    ret += sum(gain[:F])
    return ret

print(solution([4, 2, 1], [2,5,3], 2))
print(solution([7, 1, 4, 4], [5, 3, 4, 3], 2))
print(solution([5, 5, 5], [5, 5, 5], 1))
