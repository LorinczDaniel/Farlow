import pygame
from lib.definitions import *
class Character:
    def __init__(self):
        self.pos_x = 8
        self.pos_y = 0
        self.image = CHARACTER_NORMAL
        self.move_index = 0
        self.attack_index = 0

    def move(self, collision_points): 
        key_input = pygame.key.get_pressed()
        character_idle = False
        if key_input[pygame.K_LEFT]:
            self.pos_y -= 1
            if(self._collide(collision_points, self.pos_x, self.pos_y) or self.pos_y < 0):
                self.pos_y += 1
            self.move_index += 1
        elif key_input[pygame.K_RIGHT]:
            self.pos_y += 1
            if(self._collide(collision_points, self.pos_x, self.pos_y)):
                self.pos_y -= 1
            self.move_index += 1
        elif key_input[pygame.K_UP]:
            self.pos_x -= 1
            if(self._collide(collision_points, self.pos_x, self.pos_y) or self.pos_x < 0):
                self.pos_x += 1
            self.move_index += 1
        elif key_input[pygame.K_DOWN]:
            self.pos_x += 1
            if(self._collide(collision_points, self.pos_x, self.pos_y)):
                self.pos_x -= 1
            self.move_index += 1
        else:
            character_idle = True
        if self.move_index > 5:
            self.move_index = 0
        if character_idle:
            self.image = CHARACTER_NORMAL
        else:
            self.image = CHARACTER_WALK[self.move_index]

        return self.pos_x, self.pos_y
    
    def _collide(self, collision_points, x, y):
        for x_i in range(len(collision_points[0])):
            if collision_points[0][x_i] == x and collision_points[1][x_i] == y:
                print("Collide")
                return True
        return False
    
    def attack(self):
        key_input = pygame.key.get_pressed()
        if(key_input[pygame.K_a]):
            if self.attack_index > 2:
                self.attack_index = 0
            self.image = CHARACTER_ATTACK[self.attack_index]
            self.attack_index += 1
        else: self.image = CHARACTER_NORMAL
            


        


            