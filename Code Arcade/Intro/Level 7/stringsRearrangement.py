from itertools import permutations


def solution(inputArray):
    perms = permutations(inputArray)
    
    for perm in perms:
        if testPerm(perm):
            return True
    
    return False
    
    
def testPerm(perm):
    for i, element in enumerate(perm[:-1]):
        # essentially Levenshtein/edit distance for special case of 1
        if sum([x != y for x, y in zip(element, perm[i+1])]) != 1:
            return False
            
    return True
