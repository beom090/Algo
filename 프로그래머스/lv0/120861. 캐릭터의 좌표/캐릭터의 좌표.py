def solution(keyinput, board):
    answer = [0,0]
    
    for idx_move in range(len(keyinput)):
        if keyinput[idx_move] == "left":
            answer[0] = max(answer[0] - 1, -1 * int((board[0]-1)/2))
        elif keyinput[idx_move] =="down":
            answer[1] = max(answer[1]-1,-1*int((board[1]-1)/2))
        elif keyinput[idx_move] =="right":
            answer[0] = min(answer[0] + 1, int((board[0]-1)/2))
        elif keyinput[idx_move] =="up":
            answer[1] = min(answer[1]+1,int((board[1]-1)/2))
        else:
            print("error")
    return answer