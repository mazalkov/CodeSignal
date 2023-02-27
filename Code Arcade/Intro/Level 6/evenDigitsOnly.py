def solution(n):

    checks = [int(x) % 2 for x in str(n)]
    
    
    # split across lines for readability
    return all(c == 0 for c in checks)
