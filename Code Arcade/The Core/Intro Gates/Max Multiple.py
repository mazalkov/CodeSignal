def solution(divisor, bound):

    for N in range(bound, 0, -1):
        
        if (N % divisor) == 0:
            return N
            
    # a solution is guaranteed,
    # but good for error handling        
    return -1
