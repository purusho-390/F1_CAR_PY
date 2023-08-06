import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Car properties
CAR_WIDTH = 50
CAR_HEIGHT = 100
CAR_SPEED = 5

# Obstacle properties
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50
OBSTACLE_SPEED = 3

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('F1 Car Game')

# Load car image
car_img = pygame.image.load('car.png')
car_img = pygame.transform.scale(car_img, (CAR_WIDTH, CAR_HEIGHT))

# Clock for controlling the game loop
clock = pygame.time.Clock()

def create_obstacle():
    obstacle_x = random.randint(0, SCREEN_WIDTH - OBSTACLE_WIDTH)
    obstacle_y = -OBSTACLE_HEIGHT
    return pygame.Rect(obstacle_x, obstacle_y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)

def main():
    car_x = SCREEN_WIDTH // 2 - CAR_WIDTH // 2
    car_y = SCREEN_HEIGHT - CAR_HEIGHT

    obstacles = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car_x > 0:
            car_x -= CAR_SPEED
        if keys[pygame.K_RIGHT] and car_x < SCREEN_WIDTH - CAR_WIDTH:
            car_x += CAR_SPEED

        # Add new obstacle every few frames
        if random.randint(1, 100) < 5:
            obstacles.append(create_obstacle())

        # Move obstacles down the screen
        for obstacle in obstacles:
            obstacle.y += OBSTACLE_SPEED
            if obstacle.y > SCREEN_HEIGHT:
                obstacles.remove(obstacle)

        # Check for collision with obstacles
        for obstacle in obstacles:
            if pygame.Rect(car_x, car_y, CAR_WIDTH, CAR_HEIGHT).colliderect(obstacle):
                pygame.quit()
                sys.exit()

        # Update the screen
        screen.fill(BLACK)

        # Draw the car
        screen.blit(car_img, (car_x, car_y))

        # Draw the obstacles
        for obstacle in obstacles:
            pygame.draw.rect(screen, WHITE, obstacle)

        pygame.display.flip()
        clock.tick(60)

score = 0

# Font
font = pygame.font.SysFont(None, 36)

def show_game_over_popup():
    global score
    popup_font = pygame.font.SysFont(None, 60)
    game_over_text = popup_font.render("Game Over!", True, WHITE)
    score_text = font.render(f"Your Score: {score}", True, WHITE)
    popup_rect = pygame.Rect(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    pygame.draw.rect(screen, BLACK, popup_rect)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 3))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car_x > 0:
            car_x -= CAR_SPEED
        if keys[pygame.K_RIGHT] and car_x < SCREEN_WIDTH - CAR_WIDTH:
            car_x += CAR_SPEED

        # ... (previous code)

        # Check for collision with obstacles
        for obstacle in obstacles:
            if pygame.Rect(car_x, car_y, CAR_WIDTH, CAR_HEIGHT).colliderect(obstacle):
                show_game_over_popup()
                car_x = SCREEN_WIDTH // 2 - CAR_WIDTH // 2
                car_y = SCREEN_HEIGHT - CAR_HEIGHT
                obstacles.clear()
                score = 0

        # Update the screen
        screen.fill(BLACK)

        # Draw the car
        screen.blit(car_img, (car_x, car_y))

        # Draw the obstacles
        for obstacle in obstacles:
            pygame.draw.rect(screen, WHITE, obstacle)

        # Draw score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()
