def solutionSlow(S):
    #segs[j] is the count of segments end at i with colors represented by 
    #the binary form of j where 0 means the color has even lights, 1 odd lights
    segs = [0] * 1024
    good = [0,1,2,4,8,16,32,64,128,256,512]
    result = 0
    m = 1000000007
    for ch in S:
        color = ord(ch)-ord('0')
        tmp = [0]*1024
        tmp[1<<color] = 1
        for k in range(1024):
            j = k ^ (1<<color)
            tmp[j] += segs[k]
            #copy data from segs to tmp is low effecient,
            #because all number remain unchanged except one.
            #what we really need is mapping the index.
        for k in good:
            result = (result + tmp[k]) % m
        segs = tmp
    return result

def solution(S):
    segs = [0] * 1024
    good = [0,1,2,4,8,16,32,64,128,256,512]
    result = 0
    m = 1000000007
    mask = 0
    for ch in S:
        color = ord(ch)-ord('0')
        mask ^= (1<<color)
        #original index ^ mask = current index
        #current index ^ mask = original index
        segs[(1<<color) ^ mask] += 1
        for index in good:
            result = (result + segs[index ^ mask]) % m
    return result

print(solution("02002"))
