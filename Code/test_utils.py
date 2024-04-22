import numpy as np

from board import Board
from copy import deepcopy


def apply_all_possible_moves(player, grid=None):
    board = Board()
    if grid is not None:
        board.board = grid
    
    for i in range(board.size * board.size):
        if board.board[i] == 0:
            print("Move: ", i // board.size, i % board.size)
            board_copy = deepcopy(board)
            board_copy.apply_move(i, player)
            
            
            board_copy.display_board()
            
def find_all_valid_moves_and_apply(player, grid=None):
    board = Board()
    if grid is not None:
        board.board = grid
    
    print("Original board: ")
    board.display_board()
    
    for move in board.get_possible_moves(player):
        print("Move: ", move // board.size + 1, move % board.size + 1)
        board_copy = deepcopy(board)
        board_copy.apply_move(move, player)
        board_copy.display_board()



position = np.array([0,  0,  0,  0,  0,  0,  0,  0, 0,  0,  0,  0,  0,  0,  0,  0, 0,  0,  0,  0,  0,  0,  0,  0, 0,  0,  0,  1,  1,  0,  0,  0, 0, -1,  1,  1,  0,  1,  -1,  0, 0,  0,  0,  0,  1,  1,  0,  0, 0,  0,  0,  0,  1,  0,  1,  0, 0,  0,  0,  0,  0,  0,  0, -1] )
#apply_all_possible_moves(position)
find_all_valid_moves_and_apply(-1, position)

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