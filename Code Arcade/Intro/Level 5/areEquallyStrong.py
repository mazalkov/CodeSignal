def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    
    yours = sorted([yourLeft, yourRight])
    friends = sorted([friendsLeft, friendsRight])
    
    
    return yours == friends
