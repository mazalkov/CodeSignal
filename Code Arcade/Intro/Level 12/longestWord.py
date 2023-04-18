def solution(text):

    cur = ""
    res = ""
    
    for c in text:
        if c.isalpha():
            cur += c            
            
        else:
            l = len(cur)
            res = cur if max(len(res), l) == l else res  
            cur = ""
            
    if len(cur) > len(res):
        return cur
          
          
    return res
