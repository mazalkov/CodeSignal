def solution(year):
    
    res = 0
    
    if year % 100 == 0:
        res = (year // 100)
        
    else:
        res = (year // 100) + 1
        
        
    return res
