import pygame

# Initialize pygame
pygame.init()

# Create the screen (width, height)
screen = pygame.display.set_mode((800,600)) 

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

# Placing the spaceship in screen
def player(x, y):
    screen.blit(playerImg, (x, y))

# Game loop
running = True
while running:
# RGB = red, green, blue  mixing of colours, 255 is max
    screen.fill((255, 255, 255))
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

    # Update the screen
    pygame.display.update() 