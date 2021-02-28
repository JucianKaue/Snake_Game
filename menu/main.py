import pygame
from game.main import run_game

try:
    pygame.init()
except:
    print('pygame não foi iniciado corretamente.')

gamemodes_img = {
    'truck': pygame.image.load("images/truck.jpg"),
    'snake': pygame.image.load("images/snake.jpg"),
    'correios': pygame.image.load("images/correios.jpg")
}

screen = pygame.display.set_mode((400, 500))
screen.fill('#127996')

# Define os textos
font_title = pygame.font.SysFont('mvboli', 45, (0, 0, 0))
title = font_title.render('SNAKE GAME', True, (0, 0, 0))
font_text = pygame.font.SysFont('mvboli', 20, (0, 0, 0))
text = font_text.render('Selecione o seu nível: ', True, (0, 0, 0))
screen.blit(title, (25, 5))
screen.blit(text, (10, 60))

# Define as imagens
screen.blit(gamemodes_img['snake'], (25, 100))
screen.blit(gamemodes_img['truck'], (25, 210))
screen.blit(gamemodes_img['correios'], (25, 320))
pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if pygame.mouse.get_pressed()[0] == 1:
            mouse_position = pygame.mouse.get_pos()
            if (mouse_position[0] > 25 and mouse_position[1] > 100) and (mouse_position[0] < 375 and mouse_position[1] < 200):
                run_game('snake')
            elif (mouse_position[0] > 25 and mouse_position[1] > 210) and (mouse_position[0] < 375 and mouse_position[1] < 310):
                run_game('truck')
            elif (mouse_position[0] > 25 and mouse_position[1] > 320) and (mouse_position[0] < 375 and mouse_position[1] < 420):
                run_game('correios')

