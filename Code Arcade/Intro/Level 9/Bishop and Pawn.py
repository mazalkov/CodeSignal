def solution(bishop, pawn):
    
    letter_comp = abs(int(bishop[1])-int(pawn[1]))
    number_comp = abs(ord(bishop[0])-ord(pawn[0]))


    return letter_comp == number_comp
