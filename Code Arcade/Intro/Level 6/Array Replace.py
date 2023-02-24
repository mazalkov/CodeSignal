def solution(inputArray, elemToReplace, substitutionElem):

    for i, element in enumerate(inputArray):
      
        if element == elemToReplace:
            inputArray[i] = substitutionElem
            
            
    return inputArray
