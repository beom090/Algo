import numpy as np
from collections import Counter

def solution(board):
    length = len(board)
    
    padded_board = np.pad(board, ((1,1),(1,1)), constant_values = -1)
    
    danger_board = np.pad(board, ((1,1),(1,1)), constant_values = -1)
    
    for idx_row in range(1, length + 1):
        for idx_col in range(1, length + 1):
            if padded_board[idx_row][idx_col] == 1:
                for x in range(idx_row - 1, idx_row + 2):
                    for y in range(idx_col - 1,idx_col + 2):
                        danger_board[x][y] = 1
                        
    return Counter(danger_board.reshape(1,-1).squeeze())[0]