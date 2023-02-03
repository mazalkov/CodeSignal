def solution(inputString):

    stack = []
    
    for c in inputString:
        if c == ")":
            temp = ""
            
            while stack[-1] != "(":
                temp += stack.pop()
                
            stack.pop()
            
            for item in temp:
                stack.append(item)
                
        else:
            stack.append(c)
            
        
    return "".join(stack)
