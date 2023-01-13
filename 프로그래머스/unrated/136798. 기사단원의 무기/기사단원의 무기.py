def solution(number, limit, power):
    answer=0
    for i in range(1,number+1):
        x=Div(i)
        if x>limit:
            answer+=power
        else:
            answer+=x
    return answer

def Div(x):
    #input n, output n의 약수 갯수
    cnt=0
    for i in range(1,int(x**(1/2))+1):
        if x%i==0:
            cnt+=1
            if ((i**2)!=x):
                cnt+=1
    return cnt
