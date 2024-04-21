import numpy as np

class Board:
    
    symbols = {0: ' ', 1: 'B', -1: 'W'}
    
    def __init__(self, size=8):
        self.size = size
        self.board = np.zeros(size * size, dtype=int)
        self.init_board()
        
    def init_board(self):
        # Sets up the initial configuration in the center
        m1 = self.size * (self.size // 2) + (self.size // 2)
        m2 = self.size * (self.size // 2 -1) + (self.size // 2 - 1)
        m3 = self.size * (self.size // 2) + (self.size // 2 - 1)
        m4 = self.size * (self.size // 2 -1) + (self.size // 2)
        
        self.board[[m1, m2]] = -1
        self.board[[m3, m4]] = 1
        
    def get_cell(self, x, y):
        return self.board[x * self.size + y]
    
    def set_cell(self, x, y, value):
        self.board[x * self.size + y] = value
        
    def display_board(self):
         for i in range(self.size):
            print(' '.join([self.symbols[self.board[i * self.size + j]] for j in range(self.size)]))
        
if __name__ == '__main__':
    board = Board()
    board.display_board()