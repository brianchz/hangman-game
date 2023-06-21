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
hangman_images = []
for i in range(7):
    image = pygame.image.load("hangman_" + str(i)+ ".png")
    scaled_image = pygame.transform.scale(image, (640, 480))
    hangman_images.append(scaled_image)


guesses = []
word = "Orgrimmar".upper()
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (136,8,8)

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
    
run = True

while run:
    clock.tick(FPS)
    DISPLAY.blit(BACKGROUND, (0,0))
    DISPLAY.blit(hangman_images[hangman_status], (0,0))
    display_word()
    display_guesses()
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