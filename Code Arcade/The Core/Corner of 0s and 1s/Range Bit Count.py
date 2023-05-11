def solution(a, b):
    
    total = ""

    for i in range(a, b+1):
        total += bin(i)
        
        
    # could be a lot cleaner
    return total.count("1")
