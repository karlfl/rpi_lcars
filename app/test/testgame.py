import sys
import pygame
import random

scr_width = 800
scr_height = 600
screen = pygame.display.set_mode((scr_width, scr_height))


# Ball
ballImg = []
ballX = []
ballY = []
num_of_balls = 4
for i in range(num_of_balls):
    ballImg.append(pygame.image.load('./assets/tab.png'))
    ballX.append(random.randint(0, 736))
    ballY.append(random.randint(50, 535))

#'''This code is above the while running loop'''
def ball(x, y, i):
    screen.blit(ballImg[i], (x, y))

running = True
while running:
#'''The key stuff and what not'''
#'''I have the screen color load before the image appears'''
    for i in range(num_of_balls):
         ball(ballX[i], ballY[i], i)
    for event in pygame.event.get():   # process OS messages
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()
           break

    pygame.display.update()