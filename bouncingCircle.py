import pygame
import random

class Balls:
    def __init__(self):
        super().__init__()

pygame.init()
window = pygame.display.set_mode(800, 600)
end = False
clock = pygame.time.Clock()
while not end:
    window.fill((0,0,0))

    pygame.display.flip()
    clock.tick(30)