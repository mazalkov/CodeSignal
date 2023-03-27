def solution(votes, k):
    
    # if there are no extra votes and there is only one
    # most voted for electee, there is only one winner
    if k == 0 and sorted(votes)[-1] != sorted(votes)[-2]:
         return 1
    
    res = 0

    highest = max(votes)
    
    for v in votes:
        if v + k > highest:
            res += 1
            
            
    return res
