def solution(inputString):

    l = inputString.split(".")

    if len(l) != 4:
        return False
        
    for n in l:
        
        # can't cast to digit
        if not n.isdigit():
            return False
            
        # not in range 0..255
        if int(n) not in range(256):
            return False
            
        # multiple zeros
        if n.startswith('0') and n.count('0') > 1:
            return False
            
        # leading zeros    
        if n.startswith('0') and int(n) != 0:
            return False
            
            
    return True
