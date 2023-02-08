def solution(a, b):

    L = len(a)
    count = 0
    
    check_a = []
    check_b = []
    
    for i in range(L):
        if a[i] != b[i]:
            
            if count < 2:
                check_a.append(a[i])
                check_b.insert(0, b[i])
                count += 1
                
            else:
                return False
                
    
    if count == 0:
        return True
                
    elif count == 1:
        return False
        
    else:
        return check_a == check_b
