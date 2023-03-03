def solution(n, firstNumber):

    # n will always be an even, +ve integer,
    # therefore take half of n and add it to
    # firstNumber. take modulo in case of "overflow"
    
    return (n // 2 + firstNumber) % n
