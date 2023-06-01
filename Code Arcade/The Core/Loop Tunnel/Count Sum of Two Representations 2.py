def solution(n, l, r):

    j = l
    k = l
    
    while j + k != n and j < r:
        
        if k < r: 
            k += 1
            
        else: 
            j += 1

    if j + k != n: return 0


    return ((k-j) // 2) + 1
