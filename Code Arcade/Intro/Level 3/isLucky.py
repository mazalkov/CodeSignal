def solution(n):
    
    s = str(n)
    L = len(s)

    first_half = s[:(L//2)]
    second_half = s[(L//2):]
    
    first_sum = sum([int(i) for i in first_half])
    second_sum = sum([int(i) for i in second_half])
    
    res = first_sum == second_sum
    
    
    return res
