def solution(inputArray):

    total = 0
    
    for i, n in enumerate(inputArray[:-1]):
        if inputArray[i] >= inputArray[i+1]:
            diff = (inputArray[i]+1) - inputArray[i+1]
            inputArray[i+1] += diff 
            total += diff
            
            
    return total
