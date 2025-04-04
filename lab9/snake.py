import pygame
import random
import math
import sys
from pygame.locals import *  # For timer events

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WHITE_2 = (100, 100, 100)
GREEN = (156, 210, 54)
PURPLE = (175, 0, 155)
HEADCOLOR = (170, 10, 180)
RED = (160, 0, 0)
RED_W = (54, 13, 4)
BLUE = (0, 0, 255)  # For heavy food
YELLOW = (255, 255, 0)  # For light food

WINDOW_WIDTH, WINDOW_HEIGHT = 625, 625  # Surface
BLOCK_SIZE = 25

clock = pygame.time.Clock()
FPS = 4
time1 = 60

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

class Background:
    def draw(self, surface):  # background color and cells
        surface.fill(GREEN)
        for i in range(0, WINDOW_WIDTH, BLOCK_SIZE):
            for j in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
                pygame.draw.rect(screen, WHITE_2, (i, j, BLOCK_SIZE, BLOCK_SIZE), 1)

class Food:
    def __init__(self):
        self.spawn()
     
    def spawn(self):  # food position with random weight
        self.posx = random.randrange(0, WINDOW_WIDTH, BLOCK_SIZE)
        self.posy = random.randrange(0, WINDOW_HEIGHT, BLOCK_SIZE)
        
        # Randomly assign weight (1=normal, 2=heavy, 0=light)
        self.weight = random.choice([0, 1, 1, 1, 2])  # More chance for normal food
        
        # Set color based on weight
        if self.weight == 2:
            self.color = BLUE
        elif self.weight == 0:
            self.color = YELLOW
        else:
            self.color = RED
            
        # Set expiration time (in frames)
        self.lifetime = random.randint(30, 90)  # 1.5-4.5 seconds at 4 FPS
        self.active = True
    
    def update(self):
        if self.active:
            self.lifetime -= 1
            if self.lifetime <= 0:
                self.active = False
    
    def draw(self, surface):
        if self.active:
            pygame.draw.rect(surface, self.color, (self.posx, self.posy, BLOCK_SIZE, BLOCK_SIZE))
            # Draw a small indicator of remaining time
            if self.lifetime < 20:  # Blink when about to expire
                if pygame.time.get_ticks() % 500 < 250:  # Blink every 250ms
                    pygame.draw.rect(surface, WHITE, (self.posx, self.posy, BLOCK_SIZE, 3))

# ... [Rest of your existing classes remain exactly the same until the main loop] ...

bg = Background()
food = Food()
snake = Snake()
collision = Collision()
score = Score()
walls = Wall()

while True:
    bg.draw(screen)
    
    # Update food (check lifetime)
    food.update()
    
    # Only draw active food
    if food.active:
        food.draw(screen)
    else:
        food.spawn()  # Respawn when expired
    
    snake.draw(screen)
    score.draw(screen)
    walls.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:  # movement of the snake so that it won't pass through itself
            if event.key == pygame.K_UP and snake.state != "DOWN":
                snake.state = "UP"
            if event.key == pygame.K_DOWN and snake.state != "UP":
                snake.state = "DOWN"  
            if event.key == pygame.K_RIGHT and snake.state != "LEFT":
                snake.state = "RIGHT" 
            if event.key == pygame.K_LEFT and snake.state != "RIGHT":
                snake.state = "LEFT" 
            if event.key == pygame.K_p:
                snake.state = "STOP"
    
    if time1 <= 0:
        if not food.active:  # Only respawn if food is inactive
            food.spawn()
        time1 = 60

    # the snake eats (only active food)
    if food.active and collision.food_and_snake(snake, food):
        i = food.weight + 1  # Light=1, Normal=2, Heavy=3 body parts
        snake.add_body(i)
        score.increase(i)
        food.spawn()  # Get new food immediately
        time1 = 60
        
    if food.active and collision.food_and_walls(walls, food):  # if the food is inside a wall
        food.spawn()
        
    if collision.snake_and_walls(snake, walls):  # the snake hits a wall
        snake.lose()
        food.spawn()
        score.reset()
        walls.null_walls()
        walls.load_wall(level=1)
        time1 = 60

    # movement of the body and head
    if snake.state != "STOP":
        snake.move_body()
        snake.move()

    if collision.snake_and_borders(snake):
        snake.lose()
        food.spawn()
        score.reset()
        walls.null_walls()
        walls.load_wall(level=1)
        time1 = 60
            
    if collision.head_and_body(snake):
        snake.lose()
        food.spawn()
        score.reset()
        walls.null_walls()
        walls.load_wall(level=1)
        time1 = 60
        
    if score.points >= 6:
        walls.load_wall(level=2)
        
    time1 -= 1
    clock.tick(FPS)
    pygame.display.update()