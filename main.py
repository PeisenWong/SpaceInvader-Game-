import pygame
import random

# Initialize pygame
pygame.init()

# Create the screen (width, height)
screen = pygame.display.set_mode((800,600)) 

# Space background
background = pygame.image.load('background.jpg')

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('launch.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("rocket.png")
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# Enemy
enemyImg = pygame.image.load("monster.png")
enemyX = random.randint(0,800)
enemyY = random.randint(25, 100)
# Keep the movement of enemy
enemyX_change = 0.3
enemyY_change = 30

# Placing the spaceship in screen
def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

# Game loop
running = True
while running:
# RGB = red, green, blue  mixing of colours, 255 is max
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If typed the 'red cross button'
            running = False

        # Check whether any key is pressed
        if event.type  == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            if event.key == pygame.K_UP:
                playerY_change = -0.5
            if event.key == pygame.K_DOWN:
                playerY_change = 0.5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT or pygame.K_UP or pygame.K_DOWN:
                playerX_change = 0
                playerY_change = 0

# Set the boundaries of spaceship
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
        # Consider the 64 pixel spaceship
    if playerX >= 736:
        playerX = 736
    playerY += playerY_change
    if playerY <= 0:
        playerY = 0
    if playerY >= 536:
        playerY = 536
    player(playerX, playerY)

# Movement of enemy
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyY += enemyY_change
        enemyX_change= 0.3
    if enemyX >= 736:
        enemyY += enemyY_change
        enemyX_change = -0.3
    enemy(enemyX, enemyY)         

    # Update the screen
    pygame.display.update() 