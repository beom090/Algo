def solution(brown, yellow):
    for idx in range(1, yellow+1):
        if yellow % idx != 0:
            continue

        yheight = idx
        ywidth = yellow // idx

        if brown != 2 * (ywidth+1)+2 * (yheight + 1):
            continue
        else:
            return [ywidth+2, yheight+2]