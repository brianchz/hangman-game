import pygame

pygame.init()

NAME = "WoW Hangman"
WIDTH, HEIGHT = 1280, 720
FPS = 60
BACKGROUND = pygame.image.load("crossroads.jpg")

DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(NAME)


clock = pygame.time.Clock()

run = True

while run:
    clock.tick(FPS)
    guesses = []

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if len(pygame.key.name(event.key)) == 1 and pygame.key.name(event.key).isalpha():
                print(pygame.key.name(event.key))
    
    DISPLAY.blit(BACKGROUND, (0,0))
    pygame.display.flip()

pygame.quit()