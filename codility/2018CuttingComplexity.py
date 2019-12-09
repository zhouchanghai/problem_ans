#StringModification (Hard)
def solution(S, K):
    if K == 0:
        return S.count("M")
    n = len(S)
    countL = [0]*(n+1) # the extra one is used as countL[-1]
    toM, toL = n, 0
    start = 0
    for i, ch in enumerate(S):
        countL[i] = countL[i-1] + (1 if ch == 'L' else 0)
        if i >= K-1:
            #change S[i-K+1 ... i] to M
            change = countL[i] - countL[i-K]
            if i < n-1 and S[i+1] == 'M':
                change += 1
            if i-K >= 0 and S[i-K] == 'M':
                change += 1
            toM = min(toM, change)

        if ch != S[start]:
            if S[start] == 'M':
                toL += (i-start)//(K+1)
            start = i
    if S[start] == 'M':
        toL += (n-start)//(K+1)
    return max(toM, toL)

print(solution("MLM", 2)) #2
print(solution("MLMMLLM", 3)) #1
print(solution("MLMMMLMMMM", 2)) #2
print(solution("MLMMLLM", 0)) #4
print(solution("MLMMLLM", 7)) #3
print(solution("L", 0)) #0
print(solution("L", 1)) #1
print(solution("M", 0)) #1
print(solution("M", 1)) #0

