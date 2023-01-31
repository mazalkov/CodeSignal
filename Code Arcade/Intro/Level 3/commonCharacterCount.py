from collections import Counter


def solution(s1, s2):

    c1 = Counter(s1)
    c2 = Counter(s2)
    
    intersection = (c1 & c2).elements()
    
    res = len(list(intersection))

    return res
