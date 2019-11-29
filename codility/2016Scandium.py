def solution(A):
    n = len(A)
    if n == 1:
        return "NO SOLUTION" if A[0] % 2 else "0,0"

    first1, last1 = -1,-1
    firstLeft, firstRight, lastLeft, lastRight = 0,0,0,0
    total = 0
    for i in xrange(n):
        if A[i] % 2:
            total += 1
            if first1 < 0:
                first1, last1 = i, i
            else:
                last1 = i
                lastLeft = lastRight
                lastRight = 0
        else: #A[i] is even
            if first1 < 0:
                firstLeft += 1
                lastLeft += 1
            elif first1 == last1:
                firstRight += 1
                lastRight += 1
            else:
                lastRight += 1

    if total % 2 == 0:
        return "0,%d" % (n-1)
    elif first1 == last1:
        if firstLeft == firstRight:
            return "NO SOLUTION"
        elif firstLeft > firstRight:
            return "0,%d" % (firstLeft-firstRight-1)
        else:
            return "%d,%d" % (first1 + 1, n-firstLeft-1)
    elif A[-1] % 2:
        return "0,%d" % (n-2)
    else:
        if lastLeft >= lastRight:
            return "0,%d" % (n-lastRight*2-2)
        elif firstLeft + lastLeft >= lastRight:
            return "%d,%d" % (lastRight-lastLeft, n-lastRight-lastLeft-2)
        else:
            return "%d,%d" % (first1+1, n-firstLeft-1)
