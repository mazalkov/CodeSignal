def solution(inputArray):

    max_len = 0
    res = []
    
    for s in inputArray:
        if len(s) > max_len:
            max_len = len(s)
            
    for s in inputArray:
        if len(s) == max_len:
            res.append(s)
            
            
    return res
