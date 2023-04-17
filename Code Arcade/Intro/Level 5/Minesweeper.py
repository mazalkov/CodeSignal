def solution(matrix):
        
    dirs = [[-1,-1], [-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1], [0, -1]]
    
    H = len(matrix)
    W = len(matrix[0])
    
    for i, row in enumerate(matrix):
        matrix[i].insert(0, 0)
        matrix[i].append(0)
    
    zeros = [0] * (W+2)
    
    matrix.insert(0, zeros)
    matrix.append(zeros)
    
    res = [[0]*W for _ in range(H)]

    for r in range(1, H+1):
        for c in range(1, W+1):
            
            n = 0

            for d in dirs:
                
                dr = r + d[0]
                dc = c + d[1]
                
                if matrix[dr][dc]:
                    n += 1

            # need to "shift" back 
            res[r-1][c-1] = n
            
            
    return res    
