def solution(n):
    answer = 0
    while True:
        if n == 0:
            return answer
        answer+=n%10
        n=n//10

    return answer