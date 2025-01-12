import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Object!")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Game clock
clock = pygame.time.Clock()
FPS = 60

# Basket properties
basket_width = 100
basket_height = 20
basket_x = WIDTH // 2 - basket_width // 2
basket_y = HEIGHT - 50
basket_speed = 10

# Falling object properties
object_width = 30
object_height = 30
object_x = random.randint(0, WIDTH - object_width)
object_y = -object_height
object_speed = 5

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the basket
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < WIDTH - basket_width:
        basket_x += basket_speed

    # Move the falling object
    object_y += object_speed

    # Check if the object is caught
    if (
            object_y + object_height >= basket_y and
            basket_x <= object_x <= basket_x + basket_width
    ):
        score += 1
        object_y = -object_height
        object_x = random.randint(0, WIDTH - object_width)
        object_speed += 0.5  # Increase difficulty

    # Check if the object falls out of bounds
    if object_y > HEIGHT:
        print("Game Over!")
        print(f"Final Score: {score}")
        pygame.quit()
        sys.exit()

    # Draw the basket
    pygame.draw.rect(screen, BLUE, (basket_x, basket_y, basket_width, basket_height))

    # Draw the falling object
    pygame.draw.rect(screen, RED, (object_x, object_y, object_width, object_height))

    # Draw the score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update the screen
    pygame.display.flip()

    # Maintain FPS
    clock.tick(FPS)

pygame.quit()
