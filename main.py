import pygame
import random
from pygame import mixer

pygame.init()   #initialise the game
screen = pygame.display.set_mode((800,600))  #window size

#background
background = pygame.image.load('background.jpg')
mixer.music.load('background.wav')
mixer.music.play(-1)

#Title and logo
pygame.display.set_caption('Space Invader')
icon = pygame.image.load('rocket.png')
pygame.display.set_icon(icon)

#player - 64x64
playerImg = pygame.image.load('space-invaders.png')
playerX = 384
playerY = 480
playerX_change=0
playerY_change=0

#score

score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

def showText(x,y):
    score = font.render('Score: ' + str(score_value) , True , (0,255,0) )
    screen.blit(score,(x,y))

#Game Over
game_over_font = pygame.font.Font('freesansbold.ttf',32)
over_x = 250
over_y = 250

def game_over_text(x,y):
    game_over = font.render('GAME OVER!!!', True , (0,255,0) )
    screen.blit(game_over,(x,y))


def player(x,y):
    screen.blit(playerImg,(x,y))

#enemy - 64x64
num_of_enemies = 6
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = 0.5

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,534))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(1)

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

#bullet - 32x32
bulletImg = pygame.image.load('bullet.png')
bulletX = 400
bulletY = 480
bulletY_change = 7
bullet_state = "ready"

numOfBulllets = 0
bulletImg = pygame.image.load('bullet.png')
bulletX = []
bulletY = []
bulletY_change = 7
#bullet_state = []


def fire_bullet(x,y,i):
    #global bullet_state
    #bullet_state[i] = "fire"
    screen.blit(bulletImg,( x , y + 10 ))


def isCollision(j,i):
    return enemyY[i]<=bulletY[j]<=enemyY[i]+40 and enemyX[i]<=bulletX[j]<=enemyX[i]+64

def resetAfterCollision(j,i):
    #collion_Sound = mixer.Sound('explosion.wav')
    #collion_Sound.play()
    global enemyY,enemyX,bulletX,bulletY,score_value,numOfBulllets
    del bulletY[j]
    del bulletX[j]
    score_value+=1
    numOfBulllets-=1
    enemyX[i] = random.randint(0,534)
    enemyY[i] = random.randint(50,150)
        

#Game loop
running = True
while(running):

    #background color
    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    #playerX+=0.01

    for event in pygame.event.get():
        #quit the window
        if(event.type == pygame.QUIT):
            running=False

        #keystroke event
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_RIGHT):
                #print('Hello')
                playerX_change = 2
                
                #playerX+=0.5
            if(event.key == pygame.K_LEFT):
                #playerX-=0.5
                playerX_change = -2
            if(event.key == pygame.K_UP):
                playerY_change = -2
            if(event.key == pygame.K_DOWN):
                playerY_change = 2

            if(event.key == pygame.K_SPACE):
                #bullet_Sound = mixer.Sound('laser.wav')
                #bullet_Sound.play()
                #bulletImg.append(pygame.image.load('bullet.png'))
                bulletX.append(playerX + 16)
                bulletY.append(playerY)
                fire_bullet(bulletX[-1],playerY,numOfBulllets)

                numOfBulllets+=1
            
        if(event.type == pygame.KEYUP):
            if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                playerX_change = 0
            if(event.key == pygame.K_UP or event.key == pygame.K_DOWN):
                playerY_change = 0

    #player boundaries
    playerX+=playerX_change
    playerY+=playerY_change

    if(playerX<0):
        playerX=0
    elif(playerX>734):
        playerX=734
    if(playerY>534):
        playerY=534
    elif(playerY<450):
        playerY=450


    for i in range(num_of_enemies):

        #Game Over
        if(enemyY[i]>playerY-62):
            for j in range(num_of_enemies):
                enemyY[j]=1000
                enemy(enemyX[j],enemyY[j],i)
                pygame.display.update()
            game_over_text(over_x,over_y)
            break

        #enemy movement
        enemyX[i]+=enemyX_change[i]
        enemyY[i]+=enemyY_change
        if(enemyX[i]<=-10):
            enemyX_change[i] = 1
            enemyY[i]+=enemyY_change
        elif(enemyX[i]>=745):
            enemyX_change[i] = -1
            enemyY[i]+=enemyY_change

        
        #collision
        for j in range(numOfBulllets):
            collision = isCollision(j,i)
            if(collision):
                resetAfterCollision(j,i)
                break

        #enemy image
        

    #bullet movement
    j = 0
    while j<numOfBulllets:
        if(bulletY[j]<-10):
            if(score_value>0):
                score_value-=1
            del bulletX[j]
            del bulletY[j]
            numOfBulllets-=1
            break

        else:
            fire_bullet(bulletX[j],bulletY[j],j)
            bulletY[j]-=bulletY_change
            j+=1

    for i in range(num_of_enemies):
        enemy(enemyX[i],enemyY[i],i)
        #pygame.display.update()

        #player image
        player(playerX,playerY)
        showText(textX,textY)
        pygame.display.update()