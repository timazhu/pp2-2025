import pygame
import datetime

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()

# Load Mickey's image and hands
mickey_body = pygame.image.load("mickey_body.png")  # Replace with your Mickey body image
minute_hand = pygame.image.load("minute_hand.png")  # Replace with your minute hand image
second_hand = pygame.image.load("second_hand.png")  # Replace with your second hand image

# Center of the screen
center = (200, 200)

def rotate_image(image, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=center).center)
    return rotated_image, new_rect

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get current time
    now = datetime.datetime.now()
    seconds = now.second
    minutes = now.minute

    # Calculate angles
    second_angle = -seconds * 6  # 360 degrees / 60 seconds = 6 degrees per second
    minute_angle = -minutes * 6  # 360 degrees / 60 minutes = 6 degrees per minute

    # Rotate hands
    rotated_second, second_rect = rotate_image(second_hand, second_angle)
    rotated_minute, minute_rect = rotate_image(minute_hand, minute_angle)

    # Draw everything
    screen.fill((255, 255, 255))
    screen.blit(mickey_body, mickey_body.get_rect(center=center))
    screen.blit(rotated_minute, minute_rect)
    screen.blit(rotated_second, second_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

import pygame
import datetime

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Clock')
clock = pygame.time.Clock()
FPS = 50
done = False
myClock = pygame.image.load('mainclock.png')
myClock = pygame.transform.scale(myClock, (600, 600))


# hour_arrow = pygame.image.load('hour.png')
# hour_arrow = pygame.transform.scale(hour_arrow, (23, 166))
minute_arrow = pygame.image.load('rightarm.png') # 30:257
minute_arrow = pygame.transform.scale(minute_arrow, (800, 700))
second_arrow = pygame.image.load('leftarm.png')
second_arrow = pygame.transform.scale(second_arrow, (40, 500))


while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        my_time = datetime.datetime.now()
        hourINT = int(my_time.strftime("%I"))
        minuteINT = int(my_time.strftime("%M"))
        secondINT = int(my_time.strftime("%S"))

        angleHOUR = (hourINT % 12 + minuteINT/60) * 30 * -1 
        angleMINUTE = minuteINT * 7 * -1 - 10
        angleSECOND = secondINT * 6 * -1 - 5

        minute = pygame.transform.rotate(minute_arrow, angleMINUTE)
        second = pygame.transform.rotate(second_arrow, angleSECOND)
        

        screen.fill((255, 255, 255))
        screen.blit(myClock, (100, 100))
        screen.blit(second, (399 - int(second.get_width() / 2), 400 - int(second.get_height() / 2))) # centering the image
        # screen.blit(hour, ((399 - int(hour.get_width() / 2), 400 - int(hour.get_height() / 2))))
        screen.blit(minute, ((399 - int(minute.get_width() / 2), 400 - int(minute.get_height() / 2))))
        pygame.draw.circle(screen, (0, 0, 0), (400, 400), 22)
        pygame.display.flip()
        clock.tick(FPS)
        # time.sleep(1)
pygame.quit()