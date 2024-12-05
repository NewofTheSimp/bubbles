import pygame
import random
class Enemy:  

    WIDTH, HEIGHT = 1280, 720
    CIRCLE_COLOR = (0, 255, 0)
    BACKGROUND_COLOR = (0, 0, 0)
    CIRCLE_SPEED = 5

    x, y = WIDTH // 3, HEIGHT // 3
    dx, dy = random.choice([-CIRCLE_SPEED, CIRCLE_SPEED]), random.choice([-CIRCLE_SPEED, CIRCLE_SPEED])


    def __init__(self, Vector1, Size, Screen):
        self.Vector1 = Vector1
        self.Size = Size
        self.Screen = Screen


    def MoveEnemy(self):
        self.x += self.dx
        self.y += self.dy

        # Bounce off the walls
        if self.x - self.Size < 0 or self.x + self.Size > self.WIDTH:
            self.dx = -self.dx
        if self.y - self.Size < 0 or self.y + self.Size > self.HEIGHT:
            self.dy = -self.dy
        self.Vector1.x = self.x
        self.Vector1.y = self.y
        return self.Vector1
        
 
        