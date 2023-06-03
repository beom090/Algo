def solution(phone_number):
    answer = ''
    temp =0 
    for i in phone_number:
        if len(phone_number) -  temp > 4:
            answer += "*"
        else:
            answer += i
        temp +=1
    return answer