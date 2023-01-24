def solution(n):

    # n1 = 1 (base case)
    # n2 = 5  = 1 + 4
    # n3 = 13 = 5 + 8
    # n4 = 25 = 13 + 12
    # n5 = 41 = 25 + 16
    # area = solution(n-1) + 4*(n-1)
    
    if n == 1:
        return 1
        
    else:
        return solution(n-1) + 4*(n-1)
    
    
