def solution(deposit, rate, threshold):

    solution = math.log(threshold/deposit) / math.log(1+(rate/100))
    
    return math.ceil(solution)
