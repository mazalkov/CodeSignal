def solution(score1, score2):

    if (score1 == 6 and score2 < 5) or (score2 == 6 and score1 < 5):
        return True
        
    if (score1 == 7 and score2 in [5, 6]) or (score2 == 7 and score1 in [5, 6]):
        return True


    return False
