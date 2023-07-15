def solution(s):
    cnt, removed_zeros = 0, 0

    while (len(s) != 1):
        count_ones = s.count('1')
        removed_zeros += len(s) - count_ones
        cnt += 1

        s = bin(count_ones)[2:]

    return [cnt, removed_zeros]