def solution(a):

    heights = [h for h in a if h != -1]
    sorted_heights = sorted(heights)
    
    for i, h in enumerate(a):
        if h != -1:
            a[i] = sorted_heights[0]
            sorted_heights.pop(0)
            
            
    return a
