import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Menu de Jogo")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0) 

background = pygame.image.load("menu.png") 

font = pygame.font.Font(None, 36)

def text_objects(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()

def button(msg, x, y, width, height, inactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, width, height))

        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, width, height))

    text_surface, text_rect = text_objects(msg, font, black)
    text_rect.center = ((x + (width / 2)), (y + (height / 2)))
    screen.blit(text_surface, text_rect)

def start_game():
    print("Em contrução")

def quit_game():
    pygame.quit()
    sys.exit()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)

    title_text, title_rect = text_objects("Entre Mundos", pygame.font.Font(None, 72), red)
    title_rect.center = (screen_width / 2, 100)
    screen.blit(title_text, title_rect)

    button("Iniciar Jogo", 300, 250, 200, 50, (0, 100, 0), (0, 255, 0), start_game)
    button("Sair do Jogo", 300, 350, 200, 50, (100, 0, 0), (255, 0, 0), quit_game)

    pygame.display.update()

pygame.quit()
sys.exit()
