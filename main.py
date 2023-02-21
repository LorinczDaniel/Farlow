import pygame
import sys
import numpy as np
from lib.definitions import *
from character.Character import Character


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, 500))
    CLOCK = pygame.time.Clock()
    character = Character()
    
    while True:
        drawGrid(character)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        CLOCK.tick(FPS)


def drawGrid(character):
    blockSize = BLOCK_SIZE #Set the size of the grid block
    map_arr = np.array(MAP)
    collision_points = np.where(map_arr=='O')
    char_x, char_y = character.move(collision_points)
    character.attack()
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            x_index = int(x / blockSize)
            y_index = int(y / blockSize)
            if MAP[x_index][y_index] == 'O':
                rect = pygame.image.load(NORMAL_TILE[0]).convert()
            elif MAP[x_index][y_index] == 'X':
                rect = pygame.image.load(ROAD_TILE).convert()
            if x_index == char_x and y_index == char_y:
                rect = pygame.image.load(character.image).convert()
            RECT_SIZED = pygame.transform.scale(rect, (BLOCK_SIZE, BLOCK_SIZE))
            SCREEN.blit(RECT_SIZED, (y,x))

main()