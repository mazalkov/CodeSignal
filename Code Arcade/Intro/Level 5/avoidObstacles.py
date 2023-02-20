def solution(inputArray):

    length = 1
    
    """
    An inelegant solution that uses a "while True" loop but 
    still works to an acceptable level of speed. For a given
    length, if every obstacle coordinate mod that length is 
    one, that means that enough "gaps" exist for the length
    to "hop" over without being stopped by an obstacle. So if
    every length is checked from 1 upwards, a minimum is found.
    """

    while True:
        if all([(element%length) for element in inputArray]):
            return length
        length += 1
