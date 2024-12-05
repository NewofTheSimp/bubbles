import pygame

pygame.init()   
# pygame setup
class Hunter:
    def __init__(self, hunter_pos, hunter_size, screen):
        self.screen = screen
        self.hunter_pos = hunter_pos
        self.hunter_size = hunter_size

    def moveHunter(self, dt):
        move_left = False
        move_right = False
        move_up = False
        move_down = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            move_up = True
        if keys[pygame.K_s]:
            move_down = True
        if keys[pygame.K_a]:
            move_left = True
        if keys[pygame.K_d]:
            move_right = True

        if move_left and self.hunter_pos.x - self.hunter_size > 0:
            self.hunter_pos.x -= 300 * dt
        if move_right and self.hunter_pos.x + self.hunter_size < self.screen.get_width():
            self.hunter_pos.x += 300 * dt
        if move_up and self.hunter_pos.y - self.hunter_size > 0:
            self.hunter_pos.y -= 300 * dt
        if move_down and self.hunter_pos.y + self.hunter_size < self.screen.get_height():
            self.hunter_pos.y += 300 * dt
        return self.hunter_pos
        
