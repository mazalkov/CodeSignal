def solution(inputString):

    res = ""

    for c in inputString:
        
        if c == "z":
            res += "a"
            
        else:
            res += chr(ord(c)+1)
        
        
    return res
