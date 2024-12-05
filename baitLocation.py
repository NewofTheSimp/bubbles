import random
import pygame
class Bait:

  def __init__ (self, screen):
    self.screen = screen

  def bait (self):
      self.bait = []
      for x in range(0, 20):
        x = random.randint(0, self.screen.get_width())
        y = random.randint(0, self.screen.get_height())
        bait_pos = pygame.Vector2(x, y)
        self.bait.append(bait_pos)
      return self.bait


        
