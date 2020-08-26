import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))

background = pygame.image.load('background.jpg')

pygame.display.set_caption('Space Invader')
icon = pygame.image.load('rocket.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('space-invaders.png')
playerX = 384
playerY = 480
playerX_change=0
playerY_change=0

def player(x,y):
    screen.blit(playerImg,(x,y))

running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running=False

        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_LEFT):
                playerX_change = -2

    playerX+=playerX_change

    player(playerX,playerY)
    pygame.display.update()
