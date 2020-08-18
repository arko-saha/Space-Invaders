
'''

The Aim is to build a space invader game using pygame module. The used resources here are open-source.
Author: Arko Saha
Date: 04 - 08 - 2020

'''


# import the modules

import pygame
import random
import math

# initialize Pygame

pygame.init()

# Logo, Title, Background

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)
background = pygame.image.load("Background.png")

# Player

playerImg = pygame.image.load("UFO.png")
playerX, playerY = 370, 480
playerXdir = 0

# Enemy

enemyImg = []
enemyX = []
enemyY = []
enemyXdir = []
enemyYdir = []
numEnemy = 5

for i in range(numEnemy):
    enemyImg.append(pygame.image.load('alien.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyXdir.append(4)
    enemyYdir.append(20)

# Bullet

bulletImg = pygame.image.load("bullet.png")
bulletX, bulletY = 0, 480
bulletXdir = 0
bulletYdir = 10
bulletState = "ready"  # Bullet Hidden


# Functions

score_value = 0
font = pygame.font.SysFont("Consolas", 32)
textX, textY = 10, 550


# Game Over

gameOver_font = pygame.font.SysFont("Consolas", 96, bold=True)


def showScore(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def gameOver():
    gameOverTxt = font.render("GAME OVER!", True, (255, 255, 255))
    screen.blit(gameOverTxt, (300, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))   # Draw on the canvas


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))   # Draw on the canvas


def fire(x, y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImg, (x+16, y+10))


def isCollision(enemyX, enemyY, bulletX, bulletY):

    # Pythagorean Theorem

    distance = math.hypot(enemyX - bulletX, enemyY - bulletY)

    # if collision occurs, return true

    if distance < 27:
        return True
    else:
        return False


# Create a screen

screen = pygame.display.set_mode((800, 600))

# Game Loop

running = True

while running:

    # Background Color

    screen.fill((0, 0, 23))

    # Background Image

    screen.blit(background, (0, 0))

    # Loop for stability of the screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard Bindings

    # If the key is pressed

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerXdir = -5
            elif event.key == pygame.K_RIGHT:
                playerXdir = 5
            elif event.key == pygame.K_SPACE:
                if bulletState is "ready":
                    bulletX = playerX
                    fire(bulletX, bulletY)

    # If the key is released

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXdir = 0

    # Player Movement

    playerX += playerXdir

    if playerX <= 0:
        playerX = 0

    elif playerX >= 736:
        playerX = 736

    # Enemy Movement

    for i in range(numEnemy):

        # Game Over

        if enemyY[i] > 435:
            for j in range(numEnemy):
                enemyY[j] = 15000
            gameOver()
            break

        enemyX[i] += enemyXdir[i]

        if enemyX[i] <= 0:
            enemyXdir[i] = 5
            enemyY[i] += enemyYdir[i]

        elif enemyX[i] >= 736:
            enemyXdir[i] = -5
            enemyY[i] += enemyYdir[i]

        # Collision

        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bulletState = "ready"
            score_value += 1
            print(score_value)
            enemyX[i], enemyY[i] = 20, random.randint(0, 70)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement

    if bulletY <= 0:
        bulletY = 480
        bulletState = "ready"

    if bulletState is "fire":
        fire(bulletX, bulletY)
        bulletY -= bulletYdir

    # Run The Functions

    player(playerX, playerY)
    showScore(textX, textY)

    # Update the Screen

    pygame.display.update()
