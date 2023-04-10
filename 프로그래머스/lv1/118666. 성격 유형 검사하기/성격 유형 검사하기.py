def solution(survey, choices):
    answer = ''
    number = [0,0,0,0]
    for i in range(len(survey)):
        if choices[i] != 4:
            if survey[i] == "AN":
                number[3]+=choices[i]-4
            elif survey[i] =="NA":
                number[3]-=choices[i]-4
            elif survey[i] == "CF":
                number[1]+=choices[i]-4
            elif survey[i] == "FC":
                number[1]-=choices[i]-4
            elif survey[i] == "JM":
                number[2]+=choices[i]-4
            elif survey[i] == "MJ":
                number[2]-=choices[i]-4
            elif survey[i] == "RT":
                number[0]+=choices[i]-4
            elif survey[i] == "TR":
                number[0]-=choices[i]-4

    if number[0]<=0:
        answer+="R"
    else:
        answer+="T"
    if number[1]<=0:
        answer += "C"
    else:
        answer += "F"
    if number[2] <= 0:
        answer += "J"
    else:
        answer+="M"
    if number[3] <= 0:
        answer+="A"
    else:
        answer+="N"
    return answer