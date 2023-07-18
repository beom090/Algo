def solution(n):
    answer = [0,1]
    num = 0
    for i in range(1,n):
        num = answer[i-1] + answer[i]
        answer.append(answer[i-1] + answer[i])
    return num % 1234567