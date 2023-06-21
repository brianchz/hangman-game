import pygame
from pygame.locals import *

pygame.init()

NAME = "WoW Hangman"
WIDTH, HEIGHT = 1280, 720
FPS = 60
BACKGROUND = pygame.image.load("crossroads.jpg")

DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(NAME)


clock = pygame.time.Clock()

hangman_status = 0
hangman_images = []
for i in range(7):
    image = pygame.image.load("hangman_" + str(i)+ ".png")
    scaled_image = pygame.transform.scale(image, (640, 480))
    hangman_images.append(scaled_image)

hangman_win = pygame.image.load("hangman_win.png")
hangman_win_scaled = pygame.transform.scale(hangman_win, (1000, 800))

guesses = []
word = "Orgrimmar".upper()
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (136,8,8)
GREEN = (0,128,0)

FONT = pygame.font.SysFont('dejavusansmono', 40)

def display_word():
    display_word = ""
    for letter in word:
        if letter in guesses:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = FONT.render(display_word, 1, BLACK)
    DISPLAY.blit(text, (700,200))

def display_guesses():
    incorrect_guesses = "Incorrect Guesses: "
    for guess in guesses:
        if guess not in word:
            incorrect_guesses += guess + " "
    text = FONT.render(incorrect_guesses, 1 , RED)
    DISPLAY.blit(text, (200, 600))
    
def display_win():
    victory_text = "Congratulations! You've won!"
    text = FONT.render(victory_text, 1, GREEN)
    DISPLAY.blit(text, (300,600))
    DISPLAY.blit(hangman_win_scaled, (100,0))

def display_loss():
    loss_text = "You Lost! Better luck next time!"
    text = FONT.render(loss_text, 1, RED)
    DISPLAY.blit(text, (300,600))
    DISPLAY.blit(hangman_images[hangman_status], (0,0))

run = True
game_in_progress = True

while run:
    clock.tick(FPS)
    DISPLAY.blit(BACKGROUND, (0,0))

    if game_in_progress:
        DISPLAY.blit(hangman_images[hangman_status], (0,0))
        display_word()
        display_guesses()
        pygame.display.flip()
    elif won:
        display_win()
        pygame.display.flip()
    else:
        display_loss()
        pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            input = pygame.key.name(event.key).upper()
            if len(input) == 1 and input.isalpha() and input not in guesses:
                guesses.append(input)
                if input not in word:
                    hangman_status += 1
    
    won = True
    for letter in word:
        if letter not in guesses:
            won = False
            break

    if won:
        game_in_progress = False

    if hangman_status == 6:
        game_in_progress = False

pygame.quit()