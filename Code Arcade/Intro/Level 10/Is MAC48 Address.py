import re


def solution(inputString):

    pattern = "^([0-9|A-F][0-9|A-F]-){5}[0-9|A-F][0-9|A-F]$"

    is_match = bool(re.match(pattern, inputString))
    
    
    return is_match
