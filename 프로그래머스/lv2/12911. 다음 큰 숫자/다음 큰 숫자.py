def solution(n):
    answer = n + 1
    bined = bin(n)[2:]
    bined = bined.count('1')
    while (True):
        answer = bin(answer)[2:]
        if answer.count('1') == bined:
            break
        answer = int(answer, 2) + 1
    return int(answer, 2)