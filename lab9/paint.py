from math import sqrt
import math
import pygame
from random import randint

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (221,160,221)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

finished = False

drawing = False

color = BLACK

prev,cur = None, None

#function for each figure
def drawRect(color, pos, width, height):  
    pygame.draw.rect(screen, color, (pos[0], pos[1], width, height), 4) 

def drawCircle(color, pos, RAD):
    pygame.draw.circle(screen, color, pos, RAD, 4)

def eraser(pos, RAD):
    pygame.draw.circle(screen, WHITE, pos, RAD)

def square(color, pos, width, height):
    # Draw a square (width and height should be equal)
    size = max(width, height)  # Use the larger dimension to make it square
    pygame.draw.rect(screen, color, (pos[0], pos[1], size, size), 4)

def r_triangle(color, start_pos, end_pos):
    # Draw a right triangle (right angle at start_pos)
    x1, y1 = start_pos
    x2, y2 = end_pos
    
    # Calculate the third point to make a right triangle
    points = [
        (x1, y1),  # Right angle corner
        (x2, y1),  # Horizontal leg
        (x1, y2)   # Vertical leg
    ]
    pygame.draw.polygon(screen, color, points, 2)

def rhombus(color, start_pos, end_pos):
    # Draw a rhombus (diamond shape)
    x1, y1 = start_pos
    x2, y2 = end_pos
    
    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2
    
    points = [
        (center_x, y1),  # Top point
        (x2, center_y),  # Right point
        (center_x, y2),  # Bottom point
        (x1, center_y)  # Left point
    ]
    pygame.draw.polygon(screen, color, points, 2)

def e_triangle(color, start_pos, end_pos):
    # Draw an equilateral triangle
    x1, y1 = start_pos
    x2, y2 = end_pos
    
    # Calculate the height of the equilateral triangle
    side_length = max(abs(x2 - x1), 10)  # Ensure minimum size
    height = (sqrt(3) / 2) * side_length
    
    # Determine orientation based on mouse movement
    if x2 > x1:  # Dragging to the right
        points = [
            (x1, y1),
            (x1 + side_length, y1),
            (x1 + side_length / 2, y1 + height)
        ]
    else:  # Dragging to the left
        points = [
            (x1, y1),
            (x1 - side_length, y1),
            (x1 - side_length / 2, y1 + height)
        ]
    
    pygame.draw.polygon(screen, color, points, 2)

RAD = 30

screen.fill(WHITE)
#positions in draw time
start_pos = 0
end_pos = 0

#change figures
mode = 0

#list of 20 different colors
all_colors = []

for _ in range(20):
    all_colors.append((randint(0,255), randint(0,255), randint(0,255)))


while not finished:
    pos = pygame.mouse.get_pos() #pointer position 

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #exiting programme
            finished = True
        
        #choose a color:
        if event.type == pygame.MOUSEBUTTONDOWN:#press (not click)
            drawing = True
            start_pos = pos #start of pressing a mouse

            if pos[0] > 20 and pos[0] < 720 and pos[1] > 20 and pos[1] < 40: #color choice
                color = screen.get_at(pos)
       
        if event.type == pygame.MOUSEBUTTONUP:#mouse was not pressed
            drawing = False
            end_pos = pos #recording of pressing the mouse

            rect_x = abs(start_pos[0] - end_pos[0])#x-difference
            rect_y = abs(start_pos[1] - end_pos[1])#y-difference
            
            if mode == 1:                              #choosing a mode
                drawRect(color, start_pos, rect_x, rect_y)
            elif mode == 3:
                drawCircle(color, start_pos, rect_x)
            elif mode == 4:
                square(color, start_pos, rect_x, rect_y)
            elif mode == 5:
                r_triangle(color, start_pos, end_pos)
            elif mode == 6:
                e_triangle(color, start_pos, end_pos)
            elif mode == 7:
                rhombus(color, start_pos, end_pos)
                
        if event.type == pygame.MOUSEMOTION and drawing:  #eraser
            if mode == 2:
                eraser(pos, RAD)
        
        if event.type == pygame.MOUSEBUTTONDOWN and mode == 0:
            prev = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEMOTION and mode == 0:
            cur = pygame.mouse.get_pos()
            if prev:
                pygame.draw.line(screen, color, prev, cur, 1)
                prev = cur
        if event.type == pygame.MOUSEBUTTONUP:
            prev = None
        
        if event.type == pygame.KEYDOWN:               #space -> next mode
            if event.key == pygame.K_SPACE:             #mode 7 + space -> mode 0
                mode += 1
                if mode == 8:
                    mode = 0
            if event.key == pygame.K_BACKSPACE:      #backspace = erase
                screen.fill(WHITE)

    w = 30  #width of 20 squares 
   
    for i, col in enumerate(all_colors):
        pygame.draw.rect(screen, col, (20 + i * w, 20, w, 20)) #colors
    
    # Display current mode
    font = pygame.font.SysFont('Arial', 20)
    mode_text = [
        "Free Drawing",
        "Rectangle",
        "Eraser",
        "Circle",
        "Square",
        "Right Triangle",
        "Equilateral Triangle",
        "Rhombus"
    ]
    text_surface = font.render(f"Mode: {mode_text[mode]}", True, BLACK)
    screen.blit(text_surface, (20, 50))
    
    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()