def solution(n):
    answer = []

    for num in range(1, n+1):
        tep = 0

        for num2 in range(num, n + 1):
            tep += num2
            if tep == n:
                answer.append(num)
                break
            elif tep >n:
                break
    return len(answer)