#BeautifulPassword (Medium)
def solution(S):
    pos = {0:-1}
    mask = 0
    result = 0
    for i, ch in enumerate(S):
        if ch <= '9':
            n = ord(ch) - ord('0')
        else:
            n = 10 + ord(ch) - ord('a')
        mask = mask ^ (1<<n)
        if mask in pos:
            result = max(result, i - pos[mask])
        else:
            pos[mask] = i
    return result

print(solution("6daa6ccaaa6d"))
print(solution("abca"))
