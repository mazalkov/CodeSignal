def solution(time):

    hours, mins = time.split(":")
    
    hours_valid = 0 <= int(hours) <= 23
    mins_valid = 0 <= int(mins) <= 59
    
    
    return hours_valid and mins_valid
