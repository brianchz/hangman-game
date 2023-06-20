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
guesses = []

def print_guess(guess):
    print(guess)

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            input = pygame.key.name(event.key)
            if len(input) == 1 and input.isalpha() and input not in guesses:
                guesses.append(input)
                print("You have guessed", ', '.join(map(str, guesses)))
    
    DISPLAY.blit(BACKGROUND, (0,0))
    pygame.display.flip()

pygame.quit()