import re


def solution(inputString):

    found = re.findall('\d+', inputString)
    total = sum([int(n) for n in found])
    
    
    return total
