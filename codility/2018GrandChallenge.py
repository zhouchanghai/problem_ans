#BalancedPassword
def solution(S):
    other = None
    start = 0
    nextStart = 0
    result = 0
    for end in range(1, len(S)):
        if S[end] != S[end-1]:
            if other is None:
                other = S[end]
            elif S[end] != other and S[end] != S[start]:
                result = max(result, longestBalance(S, start, end))
                start = nextStart
                other = S[end]
            nextStart = end
    result = max(result, longestBalance(S, start, len(S)))
    return result

#Example: aaababbab, let a=1, b=-1
#a sub string is balanced if the sum is 0
def longestBalance(s, start, end):
    pos = {0:start-1}
    total = 0
    result = 0
    for i in range(start, end):
        if s[i] == s[start]:
            total += 1
        else:
            total -= 1
        if total not in pos:
            pos[total] = i
        else:
            result = max(result, i-pos[total])
    return result

print(solution("cabbacc")) #4 abba
print(solution("abababa")) #6 ababab
print(solution("aaaaaaa")) #0
