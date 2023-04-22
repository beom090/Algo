def solution(array):
    answer = 0
    temp = 0
    for i in array:
        for j in range(i):
            temp = i%10
            i = i//10
            if temp == 7:
                answer += 1
    return answer