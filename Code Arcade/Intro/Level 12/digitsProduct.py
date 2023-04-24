import math


def solution(product):
    
    if product == 0:
        return 10

    for i in range(10000):
        
        digits_product = math.prod([int(c) for c in str(i)])
        
        if digits_product == product:
            return i
            
            
    return -1
