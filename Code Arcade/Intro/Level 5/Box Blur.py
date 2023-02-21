def solution(image):

    res = []
    
    for i in range(1, len(image)-1):
        tmp = []
        
        for j in range(1, len(image[0])-1):
            avg = image[i-1][j-1] + image[i-1][j] + image[i-1][j+1] \
               +  image[i][j-1] +   image[i][j] +   image[i][j+1] \
               +  image[i+1][j-1] + image[i+1][j] + image[i+1][j+1]
                  
            avg //= 9
            tmp.append(avg)
            
        res.append(tmp)    
        
    return res
