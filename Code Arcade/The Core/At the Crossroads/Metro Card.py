def solution(lastNumberOfDays):
    
    lookup = {
        31: [28, 30, 31],
        30: [31],
        28: [31],
    }
    
    
    return lookup[lastNumberOfDays]
