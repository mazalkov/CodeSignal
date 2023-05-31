def solution(n):
    
    res = 1
    multiplier = 1

    while res < n:
        res *= multiplier
        multiplier += 1
        
        
    return res
