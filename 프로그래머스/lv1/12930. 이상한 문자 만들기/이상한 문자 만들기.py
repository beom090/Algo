def solution(s):
    answer = s.split(' ')
    str = []
    for i in answer:
        count = 0
        for j in i:
            if count % 2 == 0:
                str.append(j.upper())
            else:
                str.append(j.lower())
            count += 1
        str.append(' ')
    str.pop()
    return ''.join(str)