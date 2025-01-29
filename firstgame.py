import pygame
import random
import sys
from colors import *
from setup import *

# Initialize Pygame
pygame.init()

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Piggy Bank Coin Collector")

# Load images
piggy_image = pygame.image.load("images/piggy.png").convert()
piggy_image.set_colorkey(WHITE)  # Make white background transparent

coin_image = pygame.image.load("images/coin.jpg").convert()
coin_image.set_colorkey(WHITE)  # Make white background transparent

background_image = pygame.image.load("images/background.jpg").convert()

# Resize images
piggy_image = pygame.transform.scale(piggy_image, (80, 80))
coin_image = pygame.transform.scale(coin_image, (40, 40))
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Piggy class
class Piggy:
    def __init__(self):
        self.image = piggy_image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2 - self.rect.width // 2
        self.rect.y = SCREEN_HEIGHT - self.rect.height - 10
        self.speed = 10

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < SCREEN_WIDTH - self.rect.width:
            self.rect.x += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Coin class
class Coin:
    def __init__(self):
        self.image = coin_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = random.randint(4, 8)

    def fall(self):
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Main game function
def main():
    clock = pygame.time.Clock()
    running = True

    # Create player (piggy bank)
    piggy = Piggy()

    # List to store falling coins
    coins = [Coin()]

    # Score and timer
    score = 0
    font = pygame.font.Font(None, 36)

    # Game timer (30 seconds)
    game_duration = GAME_DURATION
    start_ticks = pygame.time.get_ticks()

    # Game loop
    while running:
        screen.blit(background_image, (0, 0))
        keys = pygame.key.get_pressed()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Move piggy
        piggy.move(keys)

        # Update and draw coins
        for coin in coins:
            coin.fall()
            coin.draw(screen)

            # Check for collision with piggy
            if piggy.rect.colliderect(coin.rect):
                score += 1
                coins.remove(coin)

            # Remove coin if it falls off the screen
            elif coin.rect.y > SCREEN_HEIGHT:
                coins.remove(coin)

        # Add new coins
        if random.randint(1, 50) == 1:  # Random chance to spawn new coins
            coins.append(Coin())

        # Draw piggy
        piggy.draw(screen)

        # Display score and timer
        score_text = font.render(f"Score: {score}", True, BLACK)
        elapsed_seconds = (pygame.time.get_ticks() - start_ticks) // 1000
        timer_text = font.render(f"Time Left: {max(0, game_duration - elapsed_seconds)}", True, BLACK)
        screen.blit(score_text, (10, 10))
        screen.blit(timer_text, (10, 50))

        # Check if time is up
        if elapsed_seconds >= game_duration:
            running = False

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    # Display final score
    screen.blit(background_image, (0, 0))
    final_text = font.render(f"Game Over! Your Score: {score}", True, BLACK)
    restart_text = font.render("Press R to Restart or Q to Quit", True, BLACK)
    screen.blit(final_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 20))
    screen.blit(restart_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 20))
    pygame.display.flip()

    # Wait for player input to restart or quit
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_r:  # Restart game
                    main()
                elif event.key == pygame.K_q:  # Quit game
                    pygame.quit()
                    sys.exit()

# Run the game
if __name__ == "__main__":
    main()
