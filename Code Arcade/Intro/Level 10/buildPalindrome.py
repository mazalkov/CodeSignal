def solution(st):
    
    def is_palindrome(string):
        return string == string[::-1]

    for i in range(len(st)):
        
        portion = st[:i]
        check_string = st + portion[::-1]

        if is_palindrome(check_string):
            return check_string
