def solution(dots):
    if cal_slope(dots[0], dots[1]) == cal_slope(dots[2], dots[3]):
        return 1
    elif cal_slope(dots[0], dots[2]) == cal_slope(dots[1], dots[3]):
        return 1
    elif cal_slope(dots[0], dots[3]) == cal_slope(dots[1], dots[2]):
        return 1
    return 0

def cal_slope(dot_1, dot_2):
    
    slope = (dot_2[1] - dot_1[1]) / (dot_2[0]- dot_1[0])
    return slope