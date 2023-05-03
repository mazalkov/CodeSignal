import operator


def solution(a, b, c):

    
    operators = [operator.add, operator.sub, operator.mul, operator.truediv]
    
    for op in operators:
        if op(a, b) == c:
            return True
            
            
    return False
