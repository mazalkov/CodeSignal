def solution(a):

    M = ""

    for integer in a:
        padded_number = format(integer, '08b')
        M += padded_number[::-1]
        
        
    return int(M[::-1], 2)
