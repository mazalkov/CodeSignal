def solution(matrix):

    total = 0
    
    # first row can't have 0s above
    total += sum(matrix[0])
    
    to_skip = set()

    for i, row in enumerate(matrix[1:]):
        for j, col in enumerate(row):
            if matrix[i][j] == 0:
                to_skip.add(j)
                
            else:
                if j not in to_skip:
                    total += matrix[i+1][j]
                
                
    return total
