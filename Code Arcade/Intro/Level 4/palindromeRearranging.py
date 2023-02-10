from collections import Counter


def solution(inputString):
    
    vals = Counter(inputString).values()
    sorted_vals = sorted(vals)
    
    odd_found = False
    
    for v in sorted_vals:  
        if v % 2:
            if odd_found:
                return False
            else:
                odd_found = True
                
                
    return True
