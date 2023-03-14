def solution(inputArray, k):
    
    if k == 1:
        return max(inputArray)
    
    window = sum(inputArray[:k])
    res = window

    for i in range(1, len(inputArray)-k+1):
        window += inputArray[i+k-1] - inputArray[i-1]
        res = max(res, window)
        
        
    return res
