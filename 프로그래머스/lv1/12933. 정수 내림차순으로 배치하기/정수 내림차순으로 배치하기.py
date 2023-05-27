def solution(n):
    answer = 0
    temp = []
    while True:
        temp.append(n%10)
        n = n // 10
        if n == 0:
            break
    return int(''.join(map(str, sorted(temp,reverse=True))))