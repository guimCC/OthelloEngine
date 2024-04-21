from board import Board

class Game:
    directions = [-8, -7, -6, -1, 1, 6, 7, 8]
    def __init__(self):
        self.board = Board()
        self.current_player = -1
    
    def switch_player(self):
        self.current_player = -self.current_player
        
    def make_move(self, x, y):
        #self.board.set_cell(x, y, self.current_player)
        self.board.apply_move(x, y, self.current_player)
        self.switch_player()
        
    #def make_move(self, )