def solution(n):
    
    n_string = str(n)
    permutations = [int(n_string[:i] + n_string[i+1:]) for i in range(len(n_string))]
        
        
    return max(permutations)
