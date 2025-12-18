import pygame
import pygame_gui
import sys

pygame.init()

# Set up display
screen_width, screen_height = 700, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Ball")

# Set up UI
manager = pygame_gui.UIManager((700, 400))
# Create Reset Button
reset_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (100, 50)),
                                            text='Reset',
                                            manager=manager)
# Create Gravity Slider
gravity_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 50), (100, 20)),
                                            text='Gravity:')
gravity_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((0, 70), (100, 20)),
                                                    start_value=0.01,
                                                    value_range=(0.0, 0.1),
                                                    manager=manager)
# Create Friction Slider
friction_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 100), (100, 20)),
                                              text='Friction:')
friction_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((0, 120), (100, 20)),
                                                    start_value=0.999,
                                                    value_range=(1.0, 0.99),
                                                    manager=manager)

# Physics variables
GRAVITY = 0.01
FRICTION = 0.999

# Ball variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
POS_X = 300
POS_Y = 200
SPEED_X = -1
SPEED_Y = 1
RADIUS = 20

clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Handle UI events
        if event.type == pygame_gui.UI_BUTTON_PRESSED: # Check for button press
            if event.ui_element == reset_button:
                POS_X = 300
                POS_Y = 200
                SPEED_X = -1
                SPEED_Y = 1
                RADIUS = 20
        if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED: # Check for slider movement
            if event.ui_element == gravity_slider:
                GRAVITY = gravity_slider.get_current_value()
            if event.ui_element == friction_slider:
                FRICTION = friction_slider.get_current_value()
        manager.process_events(event)

    # Fill the screen with a background color
    screen.fill(BLACK)

    # Move the ball
    POS_X += SPEED_X
    POS_Y += SPEED_Y

    # Apply gravity and friction
    SPEED_Y += GRAVITY
    SPEED_Y *= FRICTION
    SPEED_X *= FRICTION

    # Bounce if the ball touches the edge of the window
    if POS_X > screen_width - RADIUS or POS_X < RADIUS + 100:
        SPEED_X *= -1
    if POS_Y > screen_height - RADIUS or POS_Y < RADIUS:
        SPEED_Y *= -1

    # Draw the ball
    pygame.draw.circle(screen, WHITE, (POS_X, POS_Y), RADIUS, 0)

    # Draw the UI
    pygame.draw.line(screen, WHITE, (100, 0), (100, screen_height), 2) # Divider line
    manager.draw_ui(screen)

    # Update the display
    pygame.display.flip()

    clock.tick(60)
    manager.update(clock.get_time())

# Quit Pygame
pygame.quit()
sys.exit()