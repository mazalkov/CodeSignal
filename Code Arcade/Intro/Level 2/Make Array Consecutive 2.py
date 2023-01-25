def solution(statues):

    minimum = min(statues) 
    maximum = max(statues)
    
    total = range(minimum, maximum+1)
    
    diff = len(set(total) - set(statues))
    
    
    return diff
