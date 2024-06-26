import numpy as np

class Board:
    
    symbols = {0: '·', 1: 'B', -1: 'W'}
    
    def __init__(self, size=8):
        self.size = size
        self.directions = [-self.size -1 , -self.size, -self.size + 1, -1, 1, self.size -1 , self.size, self.size + 1]
        
        self.board = np.zeros(size * size, dtype=int)
        self.init_board()
        # Precompute moves to edge for each cell to speed up computations when finding new moves
        self.moves_to_edge = self.compute_moves_to_edge()
        
        
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
    
    def get_cell(self, pos):
        return self.board[pos]
    
    def set_cell(self, x, y, value):
        self.board[x * self.size + y] = value
        
    def set_cell(self, pos, value):
        self.board[pos] = value
    
    def set_list_cells(self, cells, value):
        self.board[cells] = value
        
    def apply_move(self, index, player):
        
        for d in range(len(self.directions)):
        # Try to apply the move in all directions from the current cell
            turns = self.get_turns_in_direction(index, d, player)
            if turns:
                self.set_list_cells(turns + [index], player)
                #print("Turns: ", turns, "Direction: ", self.directions[d])
            
    def get_turns_in_direction(self, index, direction, player):
        
        turns = []
        i = 1
        next_index = index + self.directions[direction]
        
        while i <= self.moves_to_edge[index, direction] and self.get_cell(next_index) == -player:
            turns.append(next_index)
            next_index += self.directions[direction]
            i += 1
        
        if i <= self.moves_to_edge[index, direction] and self.get_cell(next_index) == player:
            return turns
        else:
            return []
            
        
    def get_possible_moves(self, player):
        
        moves = []
        
        for index in self.get_player_tiles(player):
            # Check all directions from the player's tiles
            for d in range(len(self.directions)):
                for i in range(1, self.moves_to_edge[index, d]):
                    next_index = index + self.directions[d] * i
                    # If the current cell is of the opposite color
                    if self.get_cell(next_index) == -player:
                        # And the next is empty, add as a possible move
                        if self.get_cell(next_index + self.directions[d]) == 0:
                            if (next_index + self.directions[d]) not in moves:
                                moves.append(next_index + self.directions[d])
                            break
                    # If the current cell is empty
                    else:
                        break
            
        return moves
                    
    
    # def apply_direction(self, index, direction, player):
    #     turns = []
        
    #     # Check if the move is valid in the given direction
    #     if self.is_valid_direction(index, direction, player, False, turns):
            
    #         self.set_cell(index, player)
    #         self.set_list_cells(turns, player)
        
        
    # def is_valid_direction(self, index, direction, player, flipping, turns):
        
    #     # Check if the move is out of bounds, skip it
    #     if not self.is_within_bounds(index, direction):
    #         return False
        
    #     # Check if  flipping is being done
    #     if not flipping:
    #         # First call on this direction. The next cell must be of the opposite color
    #         if self.get_cell(index + direction) != -player:
    #             return False
    #         else:
    #             # Recursively check the next cell in the same direction
    #             return self.is_valid_direction(index + direction, direction, player, True, turns + [index + direction])
    #     else:
    #         # Move is valid since some flipping has occurred and found a cell of current player
    #         if self.get_cell(index + direction) == player:
    #             return True
    #         # Move is invalid since some flipping has occurred and found an empty cell
    #         elif self.get_cell(index + direction) == 0:
    #             return False
    #         else:
    #             # Recursively check the next cell in the same direction
    #             return self.is_valid_direction(index + direction, direction, player, True, turns + [index + direction])

    def get_player_tiles(self, player):
        return np.where(self.board == player)[0]
    
    def compute_moves_to_edge(self):
        moves_to_edge = np.zeros((self.size * self.size, len(self.directions)), dtype=int)
        
        for i in range(self.size * self.size):
            for idx, d in enumerate(self.directions):
                steps = 0
                current_index = i
                while self.is_within_bounds(current_index, d):
                    steps += 1
                    current_index += d
                moves_to_edge[i, idx] = steps
    
        return moves_to_edge
    
    def is_within_bounds(self, current_index, direction):
        # Calculate tentative new index
        new_index = current_index + direction

        # Check bounds
        if new_index < 0 or new_index >= self.size * self.size:
            return False

        # Check not jumping over the left/right edge of the board
        if direction == -1 and current_index % self.size == 0:
            return False
        if direction == 1 and current_index % self.size == self.size - 1:
            return False
        if abs(direction) > 1:
            # Compute row differences to prevent wrapping in diagonal movements
            original_row = current_index // self.size
            new_row = new_index // self.size
            if abs(new_row - original_row) > 1:
                return False
            # Compute column differences to prevent wrapping in diagonal movements
            original_col = current_index % self.size
            new_col = new_index % self.size
            if abs(new_col - original_col) > 1:
                return False

        return True
        
    def display_board(self):
         for i in range(self.size):
            print(' '.join([self.symbols[self.board[i * self.size + j]] for j in range(self.size)]))
        
if __name__ == '__main__':
    board = Board()
    board.display_board()
    
    print(board.get_player_tiles(-1))
    moves = board.get_possible_moves(-1)
    for move in moves:
        print(move // board.size, move % board.size)
    