from collections import namedtuple

def solution(words):
    internal = [0] * 26 # daaaad
    pure = [0] * 26 # aaaa
    #(index in words, prefix or suffix size)
    Info = namedtuple('Info', ['index', 'size'])
    #select 2 longest prefix and 2 longest suffix for each letter
    prefix = [[Info(-1, 0), Info(-2, 0)] for i in range(26)]
    suffix = [[Info(-3, 0), Info(-4, 0)] for i in range(26)]
    for index in range(len(words)):
        w = words[index]
        start = 0
        for i in range(len(w)):
            if w[i] != w[start]:
                c = ord(w[start]) - ord('a')
                internal[c] = max(internal[c], i-start)
                if start == 0:
                    update(prefix[c], Info(index, size=i))
                start = i
        
        if start == 0:
            c = ord(w[0]) - ord('a')
            pure[c] += len(w)
        else:
            c = ord(w[-1]) - ord('a')
            update(suffix[c], Info(index, size=len(w)-start))

    result = max(internal)
    for c in range(26):
        size = pure[c]
        #lognest prefix and suffix in the same word
        if suffix[c][0].index == prefix[c][0].index:
            size += max(
                suffix[c][0].size + prefix[c][1].size,
                suffix[c][1].size + prefix[c][0].size)
        else:
            size += suffix[c][0].size + prefix[c][0].size
        result = max(result, size)
    return result
    
def update(max2, candidate):
    if candidate.size >= max2[0].size:
        max2[1] = max2[0]
        max2[0] = candidate
    elif candidate.size > max2[1].size:
        max2[1] = candidate

print(solution(["aabb", "aaaa", "bbab"])) #6
print(solution(["xxbxx", "xbx", "x"])) #4
print(solution(["dd", "bb", "cc", "dd"])) #4
print(solution(["daaaad", "dc", "cd"])) #4
