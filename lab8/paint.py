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
    pygame.draw.rect(screen, color, (pos[0], pos[1], width, height), 4)

def r_triangle(color, start_pos,end_pos): #formula of the right triangle
    x1=start_pos[0]
    x2=end_pos[0]                 
    y1=start_pos[1]
    y2=end_pos[1]
    pygame.draw.line(screen,color,start_pos,end_pos,2)
    pygame.draw.line(screen,color,(x1,y1),(x1,y2),2)
    pygame.draw.line(screen,color,(x1,y2),(x2,y2),2)


def rhombus(color, start_pos ,end_pos):
    x1=start_pos[0]
    x2=end_pos[0]
    delta=(abs(x1-x2)//2)//sqrt(3)
    y1=start_pos[1]
    y2=end_pos[1]
    pygame.draw.line(screen,color,(x1,y1),(x1-(delta),y2),2)
    pygame.draw.line(screen,color,(x1-(delta),y2),(x2-(delta),y2),2)
    pygame.draw.line(screen,color,(x1,y1),(x2,y1),2)
    pygame.draw.line(screen,color,(x2-(delta),y2),(x2,y1),2)


def e_triangle(color,start_pos,end_pos):
    x1=start_pos[0]
    x2=end_pos[0]
    y1=start_pos[1]
    y2=end_pos[1]
    pygame.draw.line(screen,color,start_pos,end_pos,2)
    deltax=abs(x2-x1)
    deltay=abs(y2-y1)
    x4=(deltax+x1)
    y4=(deltay+y1)
    
    y4+=deltax

    pygame.draw.line(screen,color,(x4,y4),end_pos,2)
    pygame.draw.line(screen,color,start_pos,(x4,y4),2)
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
            elif mode==4:
                if rect_x<rect_y:rect_x=rect_y
                square(color, start_pos, rect_x, rect_x)
            elif mode==5:
                r_triangle(color, start_pos,end_pos)
            elif mode==6:
                e_triangle(color, start_pos,end_pos)
            elif mode==7:
                rhombus(color, start_pos,end_pos)
        if event.type == pygame.MOUSEMOTION and drawing:  #eraser
            if mode == 2:
                eraser(pos, RAD)
        
        if event.type == pygame.MOUSEBUTTONDOWN and mode == 0:
            prev = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEMOTION and mode == 0 :
            cur = pygame.mouse.get_pos()
            if prev:
                pygame.draw.line(screen, color, prev, cur, 1)
                prev = cur
        if event.type == pygame.MOUSEBUTTONUP:
            prev = None
        
        if event.type == pygame.KEYDOWN:               #space -> next mode
            if event.key == pygame.K_SPACE:             #mode 6 + space -> mode 0
                mode += 1
                if mode==7:mode=0
            if event.key == pygame.K_BACKSPACE:      #backspace = erase
                screen.fill(WHITE)

    w = 30  #width of 20 squares 
   
    for i, col in enumerate(all_colors):
        pygame.draw.rect(screen, col, (20 + i * w, 20, w, 20)) #colors
    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()