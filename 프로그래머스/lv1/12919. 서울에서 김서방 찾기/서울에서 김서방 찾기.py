def solution(seoul):
    cnt = 0
    for i in seoul:
        if i == "Kim":
            return "김서방은 " + str(cnt) + "에 있다"
        cnt += 1