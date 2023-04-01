import os
import pygame
from pygame.locals import *
import random

#initialize pygame
pygame.init()

#set size of screen
size = width, height = (640, 420)
running = True
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Escape!")

#load images
bg = pygame.image.load(os.path.join("Assets","bg.png"))
blob1 = pygame.transform.scale(pygame.image.load(os.path.join("Assets","blob_rest.png")), (128,128))
blob2 = pygame.transform.scale(pygame.image.load(os.path.join("Assets","blob_moving.png")), (128,128))
enemy = pygame.transform.scale(pygame.image.load(os.path.join("Assets","enemy.png")), (64,64))
heart = pygame.image.load(os.path.join("Assets","heart.png"))
dead = pygame.image.load(os.path.join("Assets","heart_lost.png"))

#game variables
blob_x = width/2
blob_y = height - 120
blob_speed = 0.25
blob_width = 128
blob_height = 128
enemy_speed = 5
lives = 3
score = 0
font = pygame.font.SysFont(None,30)



while running:
    screen.blit(bg, (0, 0))
    screen.blit(heart, (0, 0))
    screen.blit(enemy, (50, 0))
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and blob_x > 0:
        blob_x -= blob_speed
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and blob_x < width - blob_width:
        blob_x += blob_speed
    if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_a] or keys[pygame.K_d]:
        screen.blit(blob2, (blob_x, blob_y))
    else:
        screen.blit(blob1, (blob_x, blob_y))
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    pygame.display.update()

pygame.quit()