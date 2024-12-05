# if xy of the circle overlaps with the circle of the bait do something
import random
import pygame
import math
class Collision:

    def __init__ (self, Vector1, Vector2, BaitSize):
        self.Vector1 =  Vector1
        self.Vector2 =  Vector2
        self.BaitSize = BaitSize + (BaitSize / 2)
    def collision(self):
        d = int(math.sqrt(math.pow(self.Vector2.y - self.Vector1.y, 2) + math.pow(self.Vector2.x - self.Vector1.x, 2)))
        if d < self.BaitSize:
            return True
        else: 
            return False