import pygame
import random
import math

class Firework:
    x = 0
    y = 800
    speed = 0
    maxHeight = 0
    nEfektu = 0
    trvanie = 1
    casSpustenia = 0
    color = ()
    def __init__(self):
        self.x = random.randint(1, 998)
        self.speed = random.randint(5, 10)
        self.maxHeight = random.randint(20, 190)
        self.nEfektu = random.randint(1, 2)
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
    def draw(self):
        pygame.draw.line(window, self.color, [self.x, self.y], [self.x, self.y + self.speed], 3)
        self.y -= self.speed
    def vybuch(self):
        if self.y <= self.maxHeight:
            #self.y = 800
            return True
    def efekt(self, seconds):
        if self.casSpustenia == 0:
            self.casSpustenia = seconds
        if self.nEfektu == 1:
            if seconds - self.casSpustenia < self.trvanie:
                pygame.draw.circle(window, self.color, (self.x, self.y), math.floor(20 + (seconds - self.casSpustenia) * 10), 3)
            else:
                return True
        elif self.nEfektu == 2:
            if seconds - self.casSpustenia < self.trvanie:
                pygame.draw.line(window, self.color, (self.x + math.floor(10 + (seconds - self.casSpustenia) * 10), self.y), (self.x + math.floor(20 + (seconds - self.casSpustenia) * 10), self.y), 3)
                pygame.draw.line(window, self.color, (self.x - math.floor(10 + (seconds - self.casSpustenia) * 10), self.y), (self.x - math.floor(20 + (seconds - self.casSpustenia) * 10), self.y), 3)
                pygame.draw.line(window, self.color, (self.x, self.y + math.floor(10 + (seconds - self.casSpustenia) * 10)), (self.x, self.y + math.floor(20 + (seconds - self.casSpustenia) * 10)), 3)
                pygame.draw.line(window, self.color, (self.x, self.y - math.floor(10 + (seconds - self.casSpustenia) * 10)), (self.x, self.y - math.floor(20 + (seconds - self.casSpustenia) * 10)), 3)
                pygame.draw.line(window, self.color, (self.x + math.floor(10 + (seconds - self.casSpustenia) * 10), self.y + math.floor(10 + (seconds - self.casSpustenia) * 10)), (self.x + math.floor(15 + (seconds - self.casSpustenia) * 10), self.y + math.floor(15 + (seconds - self.casSpustenia) * 10)), 3)
                pygame.draw.line(window, self.color, (self.x + math.floor(10 + (seconds - self.casSpustenia) * 10), self.y - math.floor(10 + (seconds - self.casSpustenia) * 10)), (self.x + math.floor(15 + (seconds - self.casSpustenia) * 10), self.y - math.floor(15 + (seconds - self.casSpustenia) * 10)), 3)
                pygame.draw.line(window, self.color, (self.x - math.floor(10 + (seconds - self.casSpustenia) * 10), self.y + math.floor(10 + (seconds - self.casSpustenia) * 10)), (self.x - math.floor(15 + (seconds - self.casSpustenia) * 10), self.y + math.floor(15 + (seconds - self.casSpustenia) * 10)), 3)
                pygame.draw.line(window, self.color, (self.x - math.floor(10 + (seconds - self.casSpustenia) * 10), self.y - math.floor(10 + (seconds - self.casSpustenia) * 10)), (self.x - math.floor(15 + (seconds - self.casSpustenia) * 10), self.y - math.floor(15 + (seconds - self.casSpustenia) * 10)), 3)
                pygame.draw.line(window, self.color, (self.x - math.floor(10 + (seconds - self.casSpustenia) * 10), self.y - math.floor(10 + (seconds - self.casSpustenia) * 10)), (self.x - math.floor(15 + (seconds - self.casSpustenia) * 10), self.y - math.floor(15 + (seconds - self.casSpustenia) * 10)), 3)
            else:
                return True


black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

window = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Nový rok 2020")
done = False
img = pygame.image.load("img/bytovky.png")
fireworks = []
for i in range(20):
    firework = Firework()
    fireworks.append(firework)
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()
while not done:
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000
    print(seconds)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    window.fill(black)
    for i in range(20):
        reach = False
        reach = fireworks[i].vybuch()
        if reach:
            skoncil = False
            skoncil = fireworks[i].efekt(seconds)
            if skoncil:
                firework = Firework()
                fireworks[i] = firework
        else:
            fireworks[i].draw()

    window.blit(img, (0, 0))

    pygame.display.flip()
    print(clock.get_rawtime())
    clock.tick_busy_loop(30)
pygame.quit()
