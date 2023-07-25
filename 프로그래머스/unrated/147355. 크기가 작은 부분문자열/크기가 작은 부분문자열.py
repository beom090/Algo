def solution(t, p):
    answer = 0
    tmp = []
    for i in range(len(t)):
        if int(t[:len(p)]) <= int(p) and len(t) >= len(p):
            answer += 1
        t = t[1:]
    return answer