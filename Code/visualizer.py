import pygame
import sys
from os import path
import numpy as np

#sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from game import Game
from board import Board


class Visualizer:
    def __init__(self, game, size=600):
        pygame.init()
        self.game = game
        self.size = size
        self.cell_size = self.size // game.board.size
        self.screen = pygame.display.set_mode((self.size, self.size))
        self.colors = {
            1: (0, 0, 0),  # Black
            -1: (255, 255, 255),  # White
            'board': (0, 130, 0),  # Green
            'grid': (20, 20, 20)   # Dark lines
        }   

    def draw_board(self):
        board_size = self.game.board.size
        for index in range(board_size * board_size):
            col = index % board_size
            row = index // board_size
            cell_x = col * self.cell_size
            cell_y = row * self.cell_size
            pygame.draw.rect(self.screen, self.colors['board'],
                             (cell_x, cell_y, self.cell_size, self.cell_size))
            cell_value = self.game.board.board[index]
            if cell_value != 0:
                pygame.draw.circle(self.screen, 
                                   self.colors[cell_value],
                                   (int(cell_x + self.cell_size / 2),
                                    int(cell_y + self.cell_size / 2)),
                                   int(self.cell_size / 2 * 0.8))

        # Draw board lines
        for i in range(board_size + 1):
            pygame.draw.line(self.screen, self.colors['grid'],
                             (0, i * self.cell_size),
                             (self.size, i * self.cell_size))
            pygame.draw.line(self.screen, self.colors['grid'],
                             (i * self.cell_size, 0),
                             (i * self.cell_size, self.size))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    running = False

            self.screen.fill((0, 0, 0))  # Clear the screen with black before redrawing
            self.draw_board()
            pygame.display.flip()  # Update the full display Surface to the screen

        pygame.quit()
        sys.exit()

# Example usage
if __name__ == "__main__":
    
    game = Game()
    viz = Visualizer(game)
    viz.run()
