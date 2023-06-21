import pygame

pygame.init()

NAME = "WoW Hangman"
WIDTH, HEIGHT = 1280, 720
FPS = 60
BACKGROUND = pygame.image.load("crossroads.jpg")

DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(NAME)


clock = pygame.time.Clock()

hangman_status = 0
guesses = []
word = "Orgrimmar".upper()
BLACK = (0,0,0)
WHITE = (255,255,255)

FONT = pygame.font.SysFont('dejavusansmono', 40)

def draw():
    display_word = ""
    for letter in word:
        if letter in guesses:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = FONT.render(display_word, 1, BLACK)
    DISPLAY.blit(text, (700,200))

run = True

while run:
    clock.tick(FPS)
    DISPLAY.blit(BACKGROUND, (0,0))
    draw()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            input = pygame.key.name(event.key).upper()
            if len(input) == 1 and input.isalpha() and input not in guesses:
                guesses.append(input)
                print("You have guessed", ', '.join(map(str, guesses)))
                if input not in word:
                    hangman_status += 1
    
    won = True
    for letter in word:
        if letter not in guesses:
            won = False
            break

    if won:
        print("won")
        break

    if hangman_status == 6:
        print("lost")
        break

pygame.quit()