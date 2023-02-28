def solution(name):

    # first character must be alphabetical or '_'
    if not name[0].isalpha() and name[0] != "_":
        return False
        
    # all other characters must be alphanumeric or '_'
    if not all([c.isalnum() or c == "_" for c in name[1:]]):
        return False
        
        
    return True
