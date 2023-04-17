def solution(inputArray):

    res = -9e10
    
    for i, elem in enumerate(inputArray[:-1]):
        if elem*inputArray[i+1] > res:
            res = elem*inputArray[i+1]
            
            
    return res
