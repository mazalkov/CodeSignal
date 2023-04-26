def solution(min1, min2_10, min11, s):

    if s < min1:
        return 0
        
    if s == min1:
        return 1
        
    if s <= min1 + (9*min2_10):
        s -= min1
        return (s // min2_10) + 1
    
    s -= min1
    s -= 9*min2_10
    
    
    return (s // min11) + 10
