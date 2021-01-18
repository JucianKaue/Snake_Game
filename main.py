import pygame


class Snake:
    def __init__(self):
        self.rows = 20
        self.columns = 18
        self.img_board = [pygame.image.load("imagens/tab-grass0.png"), pygame.image.load("imagens/tab-grass1.png")]

    def create_window(self, width, height, bg_color="#14F5CC"):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.window_size = [width, height]
        self.screen.fill(bg_color)
        pygame.display.update()

    def create_board(self, pos_board):

        pygame.draw.line(self.screen, "#000000", (30, 75), (475, 75), 15)       # Desenha a linha horizonal superior
        pygame.draw.line(self.screen, "#000000", (25, 70), (25, 575), 15)       # Desenha a linha vertical esquerda
        pygame.draw.line(self.screen, "#000000", (20, 575), (475, 575), 15)     # Desenha a linha horizonal inferior
        pygame.draw.line(self.screen, "#000000", (475, 70), (475, 575), 15)      # Desenha a linha vertical direita

        size_square = [25, 25]      # Define o tamanho de cada casa

        img_board_resized = [pygame.transform.scale(self.img_board[0], size_square),
                             pygame.transform.scale(self.img_board[1], size_square)]

        pos_square = [pos_board[0], pos_board[1]] # Cria uma lista a partir da tupla recebida

        for row in range(0, self.rows):
            # Define qual imagem começa a aparecer antes
            if row % 2 == 0:
                start_square_type = 0
            else:
                start_square_type = 1

            for column in range(0, self.columns):
                square_type = (start_square_type + column) % 2
                self.screen.blit(img_board_resized[square_type], pos_square)
                pos_square[0] += 25
            pos_square[0] = pos_board[0]
            pos_square[1] += 25
        pygame.display.update()


game = Snake()

game.create_window(500, 600, bg_color="#14F5CC")
game.create_board((25, 75))
pygame.time.wait(100000)




"""# Imagens
tab_grass_light = py.image.load("imagens/tab-grass0.png")
tab_grass_dark = py.image.load("imagens/tab-grass1.png")

tab_grass_light = py.transform.scale(tab_grass_light, (50, 50))
tab_grass_dark = py.transform.scale(tab_grass_dark, (50, 50))

# Inicia o pygame
py.init()
screen = py.display.set_mode((500, 500))

# Cria o tabuleiro
for row in range(0, 10):
    screen.blit(tab_grass_light, ())
screen.blit(tab_grass_dark, (200, 100))

py.display.update()
py.time.wait(10000)"""