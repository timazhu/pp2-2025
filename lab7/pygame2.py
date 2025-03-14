import pygame
import os

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Music Player")

music_directory = r"C:\Users\User\Desktop\PP2\lab7"
try:
    os.chdir(music_directory)
except FileNotFoundError:
    print(f"Error: Directory '{music_directory}' not found.")
    pygame.quit()
    exit()

music_files = [file for file in os.listdir() if file.endswith(".mp3")]
if not music_files:
    print("No MP3 files found in the directory.")
    pygame.quit()
    exit()

current_track = 0
paused = False
pygame.mixer.music.load(music_files[current_track])
pygame.mixer.music.play()

font = pygame.font.Font(None, 24)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True
            elif event.key == pygame.K_RIGHT:
                current_track = (current_track + 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_track])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current_track = (current_track - 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_track])
                pygame.mixer.music.play()

    screen.fill((255, 255, 255))

    instructions = font.render("Spacebar: Play/Pause, Left Arrow: Previous, Right Arrow: Next", True, (0, 0, 0))
    screen.blit(instructions, (10, 10))

    pygame.display.flip()

pygame.quit()