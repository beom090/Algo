def solution(s):
    answer = ''
    max = -200000
    min = 2000000
    answer = s.split(' ')
    for i in answer:
        if int(i) > max:
            max = int(i)
        if int(i) < min:
            min = int(i)
    
    return str(min) + " " + str(max)