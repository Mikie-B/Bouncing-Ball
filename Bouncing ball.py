import pygame
import sys

pygame.init()

# Set up display
screen_width, screen_height = 600, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Ball")

# Ball variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
POS_X = 300
POS_Y = 200
SPEED_X = 0.01
SPEED_Y = 0.01
RADIUS = 20

clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a background color
    screen.fill(BLACK)

    # Move the circle
    POS_X += SPEED_X
    POS_Y += SPEED_Y

    # Bounce if the ball touches the edge of the window
    if POS_X > screen_width - RADIUS or POS_X < RADIUS:
        SPEED_X *= -1
    if POS_Y > screen_height - RADIUS or POS_Y < RADIUS:
        SPEED_Y *= -1

    # Draw the circle
    pygame.draw.circle(screen, WHITE, (POS_X, POS_Y), RADIUS, 0)

    # Update the display to show your drawing
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()