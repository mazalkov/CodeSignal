def solution(upSpeed, downSpeed, desiredHeight):
    
    if upSpeed >= desiredHeight:
        return 1

      
    return math.ceil((desiredHeight - upSpeed) / (upSpeed-downSpeed)) + 1
