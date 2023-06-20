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
word = "Orgrimmar"
BLACK = (0,0,0)
WHITE = (255,255,255)

FONT = pygame.font.SysFont('dejavusansmono', 40)

def draw():
    display_word = ""
    for letter in word:
        if letter in guesses:
            display_word += letter + ""
        else:
            display_word += "_ "
    text = FONT.render(display_word, 1, BLACK)
    DISPLAY.blit(text, (700,200))

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
    draw()
    pygame.display.flip()

pygame.quit()