import pygame


class Board:
    def __init__(self, game_mode="city"):
        self.rows = 20
        self.columns = 18
        if game_mode == "city":
            self.img_board = [pygame.image.load("imagens/city/board/board-street-light.png"), pygame.image.load("imagens/city/board/board-street-dark.png")]

    def create_window(self, width, height, bg_color="#14F5CC"):
        try:
            pygame.init()
        except:
            print('Não foi possível iniciar o módulo PYGAME')
            return 'ERRO'
        self.screen = pygame.display.set_mode((width, height))
        self.window_size = [width, height]
        self.screen.fill(bg_color)
        pygame.display.update()

    def create_board(self, pos_board):
        pygame.draw.line(self.screen, "#000000", (20, 75), (480, 75), 10)       # Desenha a linha horizonal superior
        pygame.draw.line(self.screen, "#000000", (25, 70), (25, 575), 10)       # Desenha a linha vertical esquerda
        pygame.draw.line(self.screen, "#000000", (20, 575), (480, 575), 10)     # Desenha a linha horizonal inferior
        pygame.draw.line(self.screen, "#000000", (475, 70), (475, 580), 10)      # Desenha a linha vertical direita

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


class Player:
    def __init__(self, player_type):
        if player_type == 'TRUCK':
            self.first_part = {'RIGTH': pygame.image.load("imagens/city/caminhao/truck_right.png"),
                               'LEFT': pygame.image.load("imagens/city/caminhao/truck_left.png")}
            self.midlle_part = {'RIGTH': pygame.image.load("imagens/city/caminhao/trailer_right.png"),
                                'LEFT': pygame.image.load("imagens/city/caminhao/trailer_left.png")}
            self.last_part = {'RIGTH': pygame.image.load("imagens/city/caminhao/trailer-last_right.png"),
                              'LEFT': pygame.image.load("imagens/city/caminhao/trailer-last_left.png")}





while True:

        game = Board()

        game.create_window(500, 600, bg_color="#14F5CC")
        game.create_board((25, 75))

        pygame.time.wait(10000)
