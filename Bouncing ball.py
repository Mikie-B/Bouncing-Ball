import pygame
import pygame_gui
import sys
import random

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
                                                    value_range=(0.0, 0.1), # Note: a value of 0 means no gravity and a higher value means more gravity
                                                    manager=manager)
# Create Friction Slider
friction_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 100), (100, 20)),
                                              text='Friction:')
friction_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((0, 120), (100, 20)),
                                                    start_value=0.999,
                                                    value_range=(1.0, 0.99), # Note: a value of 1 means no friction and a lower value means more friction
                                                    manager=manager)

# Physics variables
GRAVITY = 0.01
FRICTION = 0.999

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ball class to encapsulate ball properties
class Ball:
    def __init__(self, x, y, vx, vy, radius, color=WHITE):
        self.x = float(x)
        self.y = float(y)
        self.vx = float(vx)
        self.vy = float(vy)
        self.radius = radius
        self.color = color
    def update(self):
        # Move the ball
        self.x += self.vx
        self.y += self.vy
        # Apply gravity and friction
        self.vy += GRAVITY
        self.vy *= FRICTION
        self.vx *= FRICTION
        # Bounce if the ball touches the edge of the window
        if self.x > screen_width - self.radius or self.x < self.radius + 100:
            self.vx *= -1
        if self.y > screen_height - self.radius or self.y < self.radius:
            self.vy *= -1
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius, 0)

# Create a list to hold balls
balls = [Ball(300, 200, random.uniform(-1, 1), random.uniform(-1, 1), 20)]

def spawn_ball():
    x, y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] 
    vx = random.uniform(-2, 2)
    vy = random.uniform(-1, 1)
    radius = 20
    balls.append(Ball(x, y, vx, vy, radius))

clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    dt = clock.tick(60) / 1000.0 # seconds passed since last frame

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        manager.process_events(event)

        # Handle UI events
        if event.type == pygame_gui.UI_BUTTON_PRESSED: # Check for button press
            if event.ui_element == reset_button:
                balls.clear()  # Clear all balls
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] > 100: # Only spawn ball if clicked in the main area
                spawn_ball()
        if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED: # Check for slider movement
            if event.ui_element == gravity_slider:
                GRAVITY = gravity_slider.get_current_value()
            if event.ui_element == friction_slider:
                FRICTION = friction_slider.get_current_value()

    # Fill the screen with a background color
    screen.fill(BLACK)

    # Draw and update balls
    for b in balls:
        b.update()
        b.draw(screen)

    # Draw the UI
    pygame.draw.line(screen, WHITE, (100, 0), (100, screen_height), 2) # Divider line
    manager.update(dt)
    manager.draw_ui(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()