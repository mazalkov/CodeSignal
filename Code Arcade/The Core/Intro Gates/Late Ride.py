def solution(n):

    hours = (n // 60)
    mins = (n % 60)
    
    hours_sum = sum(int(n) for n in str(hours))
    mins_sum = sum(int(n) for n in str(mins))
    
    
    return hours_sum + mins_sum
