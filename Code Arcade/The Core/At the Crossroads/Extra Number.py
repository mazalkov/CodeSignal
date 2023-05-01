def solution(a, b, c):

    if a ^ b == 0:
        return c
        
    elif a ^ c == 0:
        return b
        
    else:
        return a
      
    # could also return a^b^c but the above is slightly more redable
