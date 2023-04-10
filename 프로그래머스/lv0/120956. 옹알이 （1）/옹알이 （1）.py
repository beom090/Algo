def solution(babbling):
    answer = 0

    for b in babbling:
        for word in ['aya', 'ye', 'woo','ma']:
            b = b.replace(word,' ',1)
        if len(b.strip()) == 0:
            answer += 1
    return answer