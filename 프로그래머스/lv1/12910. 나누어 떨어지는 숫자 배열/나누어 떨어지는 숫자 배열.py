def solution(arr, divisor):
    answer = []
    temp = 0
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
            temp = 1
    if temp == 0:
        return [-1]
    answer.sort()
    return answer