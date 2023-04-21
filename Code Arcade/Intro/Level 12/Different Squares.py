def solution(matrix):
    
    seen = set()
    M, N = len(matrix), len(matrix[0])
    
    for i in range(M-1):
        for j in range(N-1):
            square = (matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1])
            seen.add(square)
            
            
    return len(seen)
