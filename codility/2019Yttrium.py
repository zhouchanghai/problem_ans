def solution(S, K):
    count = [0]*26
    distinct = 0
    for i in range(len(S)-1, -1, -1):
        c = ord(S[i]) - ord('a')
        if distinct==K and not count[c]:
            break
        count[c] += 1
        if count[c] == 1:
            distinct += 1
    else:
        return 0 if distinct==K else -1
    #S[left : right+1] is the removed part
    left, right = 0, i
    ret = right + 1
    while 1:
        if distinct == K:
            #release the left
            left += 1
            c = ord(S[left-1]) - ord('a')
            count[c] += 1
            if count[c] == 1:
                distinct += 1
            else:
                ret = min(ret, right-left+1)
        else:
            #eat the right
            right += 1
            if right >= len(S): break
            c = ord(S[right]) - ord('a')
            count[c] -= 1
            if count[c] == 0:
                distinct -= 1
                ret = min(ret, right - left + 1)
    return ret
    
print(solution("abaacbca", 2)) #3
print(solution("aabcabc", 1)) #5
print(solution("zaaaa", 1)) #1
print(solution("aaaa", 2)) #-1
