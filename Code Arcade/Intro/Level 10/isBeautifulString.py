from collections import Counter
import string 


def solution(inputString):

    c = Counter(inputString)
    
    keys = sorted(c.keys())
    
    # sort the keys and get the corresponding vals
    vals = [c[key] for key in keys]
    
    letters = string.ascii_lowercase
    LENGTH = len(keys)
    keys_str = ''.join(keys)
    
    continuity_check = letters[:LENGTH] == keys_str
    monotonicity_check = all(x>=y for x, y in zip(vals, vals[1:]))
    
    
    return continuity_check and monotonicity_check
