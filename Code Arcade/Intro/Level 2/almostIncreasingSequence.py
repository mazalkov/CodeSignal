def solution(sequence):

    flag = False
    idx = 0
    
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            if flag: 
                return False
            
            flag = True
            idx = i
            
            
    if flag:
        check = (idx == 0) or (idx+1 == len(sequence)-1) or (sequence[idx-1] < sequence[idx+1]) or (sequence[idx] < sequence[idx+2])
        
        return check
        
        
    return True
  
