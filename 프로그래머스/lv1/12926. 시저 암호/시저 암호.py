def solution(s, n):
    answer = ''
    for i in s:
        if i.isupper():
            answer += chr((ord(i)+ n - ord('A')) % 26 + ord('A'))
        elif i.islower():
            answer += chr((ord(i)+ n - ord('a')) % 26 + ord('a'))
        else:
            answer += i
    return answer