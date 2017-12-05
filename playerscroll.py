import math, random, sys
import pygame
from pygame.locals import *


# exit the program
def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN
                                  and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()


# define display surface
W = 1280
H = 700
HW = W / 2
U = H / 2
AREA = W * H

# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("code.Pylet - Scrolling Background with Player")
FPS = 500

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

bg = pygame.image.load("RESIZED 1820_1024.jpg").convert()
bgWidth, bgHeight = bg.get_rect().size

stageWidth = bgWidth
stagePosX = 0

stageHeight = 900
stagePosY = 0

startScrollingPosX = HW
startScrollingPosY = U

circleRadius = 12
circleRadius_1 = 12
circlePosX = circleRadius
circlePosY = circleRadius_1

playerPosX = circleRadius
playerPosY = circleRadius_1
playerVelocityX = 0
playerVelocityY = 0

# main loop
while True:
    events()

    k = pygame.key.get_pressed()

    if k[K_RIGHT]:
        playerVelocityX = 5
    elif k[K_LEFT]:
        playerVelocityX = -5
    elif k[K_UP]:
        playerVelocityY = -5
    elif k[K_DOWN]:
        playerVelocityY = 5
    else:
        playerVelocityX = 0
        playerVelocityY = 0

    playerPosX += playerVelocityX
    playerPosY += playerVelocityY

    if playerPosX > (stageWidth - circleRadius):
        playerPosX = stageWidth - circleRadius

    if playerPosX < circleRadius:
        playerPosX = circleRadius
    if playerPosX < startScrollingPosX:
        circlePosX = playerPosX
    elif playerPosX > stageWidth - startScrollingPosX:
        circlePosX = playerPosX - stageWidth + W
    else:
        circlePosX = startScrollingPosX
        stagePosX += -playerVelocityX

    if playerPosY > (stageHeight) - circleRadius_1:
        playerPosY = stageHeight - circleRadius_1
    if playerPosY < circleRadius_1:
        playerPosY = circleRadius_1
    if playerPosY < startScrollingPosY:
        circlePosY = playerPosY
    elif playerPosY > stageHeight - startScrollingPosY:
        circlePosY = playerPosY - stageHeight + H
    else:
        circlePosY = startScrollingPosY
        stagePosY += -playerVelocityY

    rel_x = stagePosX % bgWidth
    rel_y = stagePosY % bgHeight
    DS.blit(bg, (rel_x - bgWidth, rel_y - bgHeight))

    if rel_y < H:
        DS.blit(bg, (0, rel_y))

    if rel_x < W:
        DS.blit(bg, (rel_x, 0))

    pygame.draw.circle(DS, WHITE, (int(circlePosX), playerPosY - 25),
                       circleRadius, 0)
    pygame.draw.circle(DS, WHITE, (int(circlePosX), playerPosY - 25),
                       circleRadius_1, 0)

    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(BLACK)
