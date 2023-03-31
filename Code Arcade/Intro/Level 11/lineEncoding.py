def solution(s):
    
    # looking at next char in string,
    # so adding a dummy char to end
    s += "_"
    res = ""
    quantity = 1

    for i in range(len(s)-1):
        
        if s[i] == s[i+1]:
            quantity += 1
            
        else:
            quantity = str(quantity) if quantity != 1 else ""
            res += str(quantity) + s[i]
                
            quantity = 1
            
            
    return res
