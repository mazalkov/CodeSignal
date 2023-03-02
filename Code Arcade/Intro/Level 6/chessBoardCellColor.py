def solution(cell1, cell2):

    # For a given cell, the letter and number position of the cell
    # (e.g A1 has letter position A and number position 1) may have
    # an "odd" letter position (A, C, D, E, etc), and an "odd" number
    # position (1, 3, 5, 7, etc). Therefore, black squares will only
    # occur on cells where letter and number positions are either both
    # odd or both even. If one is even, and the other is odd, then the
    # cell must be white. We return whether both cells were found as white,
    # as if the checks both fail then we know both cells were black: True.
  
    first_is_white =  ord(cell1[0]) % 2 != int(cell1[1]) % 2

    second_is_white = ord(cell2[0]) % 2 != int(cell2[1]) % 2
        
        
    return first_is_white == second_is_white
