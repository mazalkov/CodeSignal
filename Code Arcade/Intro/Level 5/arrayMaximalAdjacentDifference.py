def solution(inputArray):
    
    max_diff = 0
    
    for i, integer in enumerate(inputArray[:-1]):
        diff = abs(integer - inputArray[i+1])
        max_diff = max(diff, max_diff)
        
        
    return max_diff
