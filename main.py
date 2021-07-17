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

# Placing the spaceship in screen
def player():
    screen.blit(playerImg, (playerX, playerY))

# Game loop
running = True
while running:
# RGB = red, green, blue  mixing of colours, 255 is max
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If typed the 'red cross button'
            running = False

    player()            

    # Update the screen
    pygame.display.update() 