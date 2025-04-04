import pygame
import random
import sys
import time

pygame.init()

FPS = 60
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
STEP = 5
ENEMTY_STEP = 5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCORE = 0

# Speed increase parameters
SPEED_INCREASE_INTERVAL = 5
SPEED_INCREMENT = 1

clock = pygame.time.Clock()
score_font = pygame.font.SysFont("Verdana", 20)

SURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Street Racer")

wasted = pygame.image.load('wasted.jpg')
wasted = pygame.transform.scale(wasted, (400, 600))

bg = pygame.image.load("AnimatedStreet.png")

pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def update(self):
        global ENEMTY_STEP
        self.rect.move_ip(0, ENEMTY_STEP)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.top = 0
            self.rect.center = (random.randint(30, 350), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-STEP, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(STEP, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.type = random.choices([1, 2, 3], weights=[0.6, 0.3, 0.1])[0]
        
        if self.type == 1:
            self.image = pygame.image.load("coin.png")
            self.image = pygame.transform.scale(self.image, (25, 25))
            self.value = 1
        elif self.type == 2:
            self.image = pygame.image.load("coin.png")
            self.image = pygame.transform.scale(self.image, (35, 35))
            self.value = 3
        else:
            self.image = pygame.image.load("coin.png")
            self.image = pygame.transform.scale(self.image, (45, 45))
            self.value = 5
            
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def update(self):
        self.rect.move_ip(0, 5)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.kill()  # Remove coin when it goes off-screen

    def draw(self, surface):
        surface.blit(self.image, self.rect)

P1 = Player()
E1 = Enemy()
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()  # Now tracks ALL coins

# Coin spawn timer
last_coin_spawn = 0
coin_spawn_interval = 2000  # milliseconds

while True:
    current_time = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Spawn new coins periodically
    if current_time - last_coin_spawn > coin_spawn_interval:
        new_coin = Coin()
        coins.add(new_coin)
        last_coin_spawn = current_time

    P1.update()
    E1.update()
    coins.update()  # Update all coins

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.music.load('crash.wav')
        pygame.mixer.music.play()
        SURF.blit(wasted, (0, 0))
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
        sys.exit()

    # Check collisions with all coins
    collected_coins = pygame.sprite.spritecollide(P1, coins, True)
    for coin in collected_coins:
        SCORE += coin.value
        if SCORE % SPEED_INCREASE_INTERVAL == 0:
            ENEMTY_STEP += SPEED_INCREMENT

    SURF.blit(bg, (0, 0))
    E1.draw(SURF)
    for coin in coins:  # Draw all coins
        coin.draw(SURF)
    P1.draw(SURF)

    score_img = score_font.render(str(SCORE), True, BLACK)
    SURF.blit(score_img, (10, 10))

    pygame.display.update()
    clock.tick(FPS)