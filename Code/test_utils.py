import numpy as np

from board import Board
from copy import deepcopy


def apply_all_possible_moves(grid=None):
    board = Board()
    if grid is not None:
        board.board = grid
    
    for i in range(board.size * board.size):
        if board.board[i] == 0:
            print("Move: ", i // board.size, i % board.size)
            board_copy = deepcopy(board)
            board_copy.apply_move(i, -1)
            
            
            board_copy.display_board()
            

apply_all_possible_moves(np.array([0,  0,  0,  0,  0,  0,  0,  0, 0,  0,  0,  0,  0,  0,  0,  0, 0,  0,  0,  0,  0,  0,  0,  0, 0,  0,  0,  1,  1,  0,  0,  0, 0, -1,  1,  1,  0,  1,  -1,  0, 0,  0,  0,  0,  1,  1,  0,  0, 0,  0,  0,  0,  1,  0,  1,  0, 0,  0,  0,  0,  0,  0,  0, -1] ))

"""
[0,  0,  0,  0,  0,  0,  0,  0,
 0,  0,  0,  0,  0,  0,  0,  0,
 0,  0,  0,  0,  0,  0,  0,  0,
 0,  0,  0,  1,  1,  0,  0,  0,
 0, -1,  1,  1,  0,  1,  -1,  0,
 0,  0,  0,  0,  1,  1,  0,  0,
 0,  0,  0,  0,  1,  0,  1,  0,
 0,  0,  0,  0,  0,  0,  0, -1]    
    
    

"""