def solution(cell):
    
    res = 0

    dirs = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    
    for horz, vert in dirs:
        if (97 <= ord(cell[0]) + horz <= 104) and (1 <= int(cell[1]) + vert <= 8):
            res += 1
            
            
    return res
