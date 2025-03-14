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
