def solution(a):

    binary = bin(a)[2:]
    reverse = binary[::-1]
    res = int(reverse, 2)
    
    return res
