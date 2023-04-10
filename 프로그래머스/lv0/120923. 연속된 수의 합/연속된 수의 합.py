def solution(num, total):
    avergae = total // num

    return [i for i in range(avergae - (num-1)//2, avergae+(num + 2)//2)]