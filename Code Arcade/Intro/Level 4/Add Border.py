def solution(picture):
    
    width = len(picture[0])
    
    # need to manipulate strings which is messy
    for i, row in enumerate(picture):
        picture[i] = "*" + picture[i] + "*"

    new_width = width + 2
    asterisks = "*" * new_width
    
    # add asterisks to top and bottom of picture
    picture.insert(0, asterisks)
    picture.append(asterisks)
    
    
    return picture
