def solution(young, beautiful, loved):
    
    first_statement = (young and beautiful) and not loved
    second_statement = loved and (not young or not beautiful)

    
    return first_statement or second_statement
