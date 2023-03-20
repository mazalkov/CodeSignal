def solution(n):
    
    res = 0

    while n > 9:
        n = sum(int(digit) for digit in str(n))
        res += 1
        
    
    return res
