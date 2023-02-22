import pygame
import sys
import numpy as np
from lib.definitions import *
from character.Player import Player


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    CLOCK = pygame.time.Clock()
    player = Player()
    
    while True:
        drawGrid(player)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        CLOCK.tick(FPS)


def drawGrid(player):
    blockSize = BLOCK_SIZE #Set the size of the grid block
    map_arr = np.array(MAP)
    collision_points = np.where(map_arr=='O')
    player.character_action(collision_points)
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            x_index = int(x / blockSize)
            y_index = int(y / blockSize)
            if MAP[x_index][y_index] == 'O':
                rect = pygame.image.load(NORMAL_TILE[0]).convert()
            elif MAP[x_index][y_index] == 'X':
                rect = pygame.image.load(ROAD_TILE).convert()
            RECT_SIZED = pygame.transform.scale(rect, (BLOCK_SIZE, BLOCK_SIZE))
            SCREEN.blit(RECT_SIZED, (y,x))

            if x_index == player.pos_x and y_index == player.pos_y:
                char = pygame.image.load(player.image)
                CHAR_SIZED = pygame.transform.scale(char, (BLOCK_SIZE, BLOCK_SIZE))
                SCREEN.blit(CHAR_SIZED, (y,x))
                


main()