import pygame
import baitLocation
import Collider
import Enemy
import Hunter
from pygame.locals import *
from tkinter import messagebox


 
# Import randint method random module
from random import randint
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

dt = 0
hunterSize = 40
enemySize = 20

hunter_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
bait = baitLocation.Bait(screen)
enemy_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
enemy = Enemy.Enemy(enemy_pos, enemySize, screen)
hunter = Hunter.Hunter(hunter_pos, hunterSize, screen)
bait = bait.bait()
won = False

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("#343131")
    enemy_pos = enemy.MoveEnemy()
    hunter_pos = hunter.moveHunter(dt)

    collisionHunt = Collider.Collision(enemy_pos, hunter_pos, hunterSize)
    collidedHunt = collisionHunt.collision()
    
    if not collidedHunt:
        pygame.draw.circle(screen, "#A04747", enemy_pos, enemySize)
        pygame.draw.circle(screen, "#EEDF7A", hunter_pos, hunterSize)
    elif enemySize < hunterSize:
        messagebox.showinfo(message="Hunter Won", title="Hunter Won")
        break
    elif enemySize > hunterSize:
        messagebox.showinfo(message="Enemy Won", title="Enemy Won")
        break




    a = []
    for b in bait:
        pygame.draw.circle(screen, "#D8A25E", b, 20)
        collisionHunter = Collider.Collision(hunter_pos, b, hunterSize)
        collisionEnemy = Collider.Collision(enemy_pos, b, enemySize)
        collidedHunter = collisionHunter.collision()
        collidedEnemy = collisionEnemy.collision() 
        if collidedHunter:
            hunterSize += 10
        elif collidedEnemy:
            enemySize += 10
        elif not collidedHunter or not collidedEnemy:
            a.append(b)
    bait = a
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()