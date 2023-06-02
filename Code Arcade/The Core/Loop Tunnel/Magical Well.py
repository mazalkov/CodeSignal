def solution(a, b, n):

    res = 0

    for _ in range(n):
        res += a*b
        a += 1
        b += 1


    return res
