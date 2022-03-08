import pygame
from pygame import *
pygame.init()
from SaveManager import SaveManager
win = pygame.display.set_mode((500, 70))
font = font.Font("Regular.ttf",40)
level = SaveManager.Load()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        level -= 1

    if keys[pygame.K_RIGHT]:
        level += 1
    
    SaveManager.Save(level)
    render = font.render(f"Level: {level}",True,(255,0,0))
    win.blit(render,Vector2(150,0))
    pygame.display.update()
    win.fill((255,255,255))