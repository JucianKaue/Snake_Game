import pygame
from random import randint


class Game:
    def __init__(self, gamemode):
        avaible_gamemodes = ["city", "truck", "correios"]
        if gamemode not in avaible_gamemodes:       # Verifica se o modo de jogo é válido.
            print('ERROR. Gamemode unavailable.\n',
                  f'Available gamemodes are: {avaible_gamemodes}')
        else:
            self.gamemode = gamemode

    @staticmethod
    def lost(player):   # Verifica se o jogador perdeu
        if player.position in player.player[0][1:]:
            return True
        else:
            return False

    @staticmethod
    def convert(to_pixels, square, size_board_pixels, size_board_squares, initial_position_board):
        size_squares = size_board_pixels//size_board_squares
        if to_pixels:
            return initial_position_board[0] + (size_squares * square[0]), initial_position_board[1] + (size_squares * square[1])
        else:
            return (square[0]-initial_position_board[0])//size_squares, (square[1]-initial_position_board[1])//size_squares

    @staticmethod
    def create_window(window_size=()):
        try:
            pygame.init()
        except:
            print("ERROR! It's not possible initialize module pygame.")
            return False
        try:
            if len(window_size) == 2:
                return pygame.display.set_mode(window_size)
            else:
                print("ERROR! WIDOWN_SIZE is invalid.")
                return False
        except:
            print("ERROR! WINDOW_SIZE needs to be a tuple.")

    @staticmethod
    def create_text(text, position, font):
        font_name = font[0]
        font_size = font[1]
        font_color = font[2]

        pygame.font.init()
        font = pygame.font.SysFont(font_name, font_size, font_color)
        screen.blit(font.render(text, True, font_color), position)
        pygame.display.update()
        pygame.font.quit()


class Player:
    def __init__(self, gamemode):
        self.position = [5, 5]
        self.direction = 'UP'
        self.length_player = 3
        self.score = self.length_player - 2
        self.player = [[], []]

        for i in range(0, self.length_player):
            print(i)
            self.player[0].append([self.position[0], self.position[1]+i])
            self.player[1].append(self.direction)

        self.size_board_pixels = 350
        self.size_board_squares = 10
        self.size_squares_pixels = self.size_board_pixels // self.size_board_squares

        default_directory_img = f'game/images/{gamemode}/player'    # Define um diretório padrão para as imagens do jogador
        self.images = {
            'First': {
                'UP': pygame.transform.scale(pygame.image.load(f'{default_directory_img}/first.png'),
                    (self.size_squares_pixels, self.size_squares_pixels)),
                'LEFT': pygame.transform.scale(pygame.transform.rotate(
                    pygame.image.load(f'{default_directory_img}/first.png'), 90),
                    (self.size_squares_pixels, self.size_squares_pixels)),
                'DOWN': pygame.transform.scale(pygame.transform.rotate(
                    pygame.image.load(f"{default_directory_img}/first.png"), 180),
                    (self.size_squares_pixels, self.size_squares_pixels)),
                'RIGHT': pygame.transform.scale(pygame.transform.rotate(
                            pygame.image.load(f"{default_directory_img}/first.png"), 270),
                                               (self.size_squares_pixels, self.size_squares_pixels)),
            },
            'Middle': {
                'UP': pygame.transform.scale(pygame.image.load(f"{default_directory_img}/middle.png"),
                                             (self.size_squares_pixels, self.size_squares_pixels)),
                'LEFT': pygame.transform.scale(pygame.transform.rotate(
                    pygame.image.load(f"{default_directory_img}/middle.png"), 90),
                    (self.size_squares_pixels, self.size_squares_pixels)),
                'DOWN': pygame.transform.scale(pygame.transform.rotate(
                    pygame.image.load(f"{default_directory_img}/middle.png"), 180),
                    (self.size_squares_pixels, self.size_squares_pixels)),
                'RIGHT': pygame.transform.scale(pygame.transform.rotate(
                    pygame.image.load(f"{default_directory_img}/middle.png"), 270),
                    (self.size_squares_pixels, self.size_squares_pixels)),

                'UP_LEFT': pygame.transform.scale(
                    pygame.image.load(f"{default_directory_img}/middle_curved.png"),
                    (self.size_squares_pixels, self.size_squares_pixels)),
                'LEFT_DOWN': pygame.transform.scale(pygame.transform.rotate(
                     pygame.image.load(f"{default_directory_img}/middle_curved.png"), 90),
                    (self.size_squares_pixels, self.size_squares_pixels)),
                'DOWN_RIGHT': pygame.transform.scale(pygame.transform.rotate(
                     pygame.image.load(f"{default_directory_img}/middle_curved.png"), 180),
                    (self.size_squares_pixels, self.size_squares_pixels)),
                'RIGHT_UP': pygame.transform.scale(pygame.transform.rotate(
                     pygame.image.load(f"{default_directory_img}/middle_curved.png"), 270),
                    (self.size_squares_pixels, self.size_squares_pixels)),

                'UP_RIGHT': pygame.transform.scale(pygame.transform.flip(
                    pygame.image.load(f"{default_directory_img}/middle_curved.png"), True, False),
                    (self.size_squares_pixels, self.size_squares_pixels)),
                'LEFT_UP': pygame.transform.scale(pygame.transform.rotate(pygame.transform.flip(
                    pygame.image.load(f"{default_directory_img}/middle_curved.png"), True, False), 90),
                    (self.size_squares_pixels, self.size_squares_pixels)),
                'DOWN_LEFT': pygame.transform.scale(pygame.transform.rotate(pygame.transform.flip(
                    pygame.image.load(f"{default_directory_img}/middle_curved.png"), True, False), 180),
                    (self.size_squares_pixels, self.size_squares_pixels)),
                'RIGHT_DOWN': pygame.transform.scale(pygame.transform.rotate(pygame.transform.flip(
                    pygame.image.load(f"{default_directory_img}/middle_curved.png"), True, False), 270),
                    (self.size_squares_pixels, self.size_squares_pixels)),
            },
            'Last': {
                'UP': pygame.transform.scale(pygame.image.load(f"{default_directory_img}/last.png"),
                                             (self.size_squares_pixels, self.size_squares_pixels)),
                'LEFT': pygame.transform.scale(pygame.transform.rotate(
                    pygame.image.load(f"{default_directory_img}/last.png"), 90),
                    (self.size_squares_pixels, self.size_squares_pixels)),
                'DOWN': pygame.transform.scale(pygame.transform.rotate(
                    pygame.image.load(f"{default_directory_img}/last.png"), 180),
                    (self.size_squares_pixels, self.size_squares_pixels)),
                'RIGHT': pygame.transform.scale(pygame.transform.rotate(
                    pygame.image.load(f"{default_directory_img}/last.png"), 270),
                    (self.size_squares_pixels, self.size_squares_pixels)),
            }
        }
        self.lost_img = pygame.image.load(f'game/images/{gamemode}/game/lost_background.jpg')
        self.score_board = pygame.image.load(f"game/images/{gamemode}/game/score_board.png")

    def move(self, board, direction):
        def actualize_score(score):
            screen.blit(self.score_board, (240, 425))
            screen.blit(pygame.transform.scale(board.target_img, (50, 50)), (240, 421))
            Game.create_text(f'{score}', (292, 426), ('mvboli', 30, (0, 0, 0)))

        def actualize_player_positions(position, list_positions):
            new_list_positions = [position]  # primeira posição do player atualizada
            for i in range(0, len(list_positions)-1):  # adiciona todas as posições atuais do player, menos a ultima
                new_list_positions.append(list_positions[i])
            return new_list_positions

        def actualize_player_directions(new_direction, old_direction, list_directions):
            new_list_directions = [direction]  # primeira posição do player atualizada
            for i in range(0, len(list_directions)-1):  # adiciona todas as posições atuais do player, menos a ultima
                # last part
                if i == len(list_directions)-2:
                    if '_' in list_directions[i]:
                        direct = list_directions[i].split('_')[1]
                        list_directions.pop(i)
                        list_directions.insert(i, direct)
                    new_list_directions.append(f'{list_directions[i]}')
                else:
                    if i == 0:
                        if not new_direction == old_direction:
                            new_list_directions.append(f'{old_direction}_{new_direction}')
                        else:
                            new_list_directions.append(list_directions[i])
                    else:
                        new_list_directions.append(list_directions[i])
            return new_list_directions

        # Confere se a direção recebida é válida
        available_directions = ['UP', 'DOWN', 'RIGHT', 'LEFT']
        if direction not in available_directions:
            print("DIREÇÃO INVÁLIDA.")
            return

        # atualiza a direção do player
        if direction == 'UP' and self.direction == 'DOWN': direction = self.direction
        if direction == 'DOWN' and self.direction == 'UP': direction = self.direction
        if direction == 'RIGHT' and self.direction == 'LEFT': direction = self.direction
        if direction == 'LEFT' and self.direction == 'RIGHT': direction = self.direction

        # Create the player list positions
        position = ()
        if direction == 'UP':
            position = (self.position[0], self.position[1] - 1)
        elif direction == 'DOWN':
            position = (self.position[0], self.position[1] + 1)
        elif direction == 'RIGHT':
            position = (self.position[0] + 1, self.position[1])
        elif direction == 'LEFT':
            position = (self.position[0] - 1, self.position[1])

        # Atualiza a nova casa inicial do player
        if position[0] < 0:
            self.position = (self.size_board_squares-1, self.position[1])

        elif position[1] < 0:
            self.position = (self.position[0], self.size_board_squares-1)
        elif position[0] > self.size_board_squares-1:
            self.position = (0, self.position[1])

        elif position[1] > self.size_board_squares-1:
            self.position = (self.position[0], 0)

        else:
            self.position = position

        # Atualiza as listas de casas e direções do jogador
        self.player[0] = actualize_player_positions(self.position, self.player[0])
        self.player[1] = actualize_player_directions(new_direction=direction,
                                                           old_direction=self.direction,
                                                           list_directions=self.player[1])
        self.direction = direction

        # Create the player images list
        images_player = []
        for i in range(0, len(self.player[0])):
            if i == 0:
                images_player.append(self.images['First'][f'{self.player[1][i]}'])
            elif i == len(self.player[0])-1:
                images_player.append(self.images['Last'][f'{self.player[1][i]}'])
            else:
                images_player.append(self.images['Middle'][f'{self.player[1][i]}'])

        # Apaga a o jogador da tela
        board.create_board(screen)

        # Mostra o jogador na sua nova posição
        for i in range(0, len(images_player)):
            screen.blit(images_player[i], Game.convert(to_pixels=True,
                                                    square=self.player[0][i],
                                                    initial_position_board=board.board_position,
                                                    size_board_squares=board.size_board_squares,
                                                    size_board_pixels=board.size_board_pixels
                                                    )
                        )

        # Verifica se o jogador está em um alvo
        if board.target_position == position:
            board.create_target(screen=screen, player_positions=self.player[0], change=True)
            self.add_part()

        actualize_score(self.score)
        pygame.display.update()

        return self.player[0]

    def add_part(self):
        self.score += 1
        self.length_player += 1
        self.player[0].append([])
        self.player[1].append(self.position)


class Board:
    def __init__(self, gamemode):

        self.board_position = (25, 50)
        self.size_board_pixels = 350
        self.size_board_squares = 10
        self.size_squares_pixels = self.size_board_pixels//self.size_board_squares

        self.board_img = [pygame.image.load(f"game/images/{gamemode}/board/board-dark.png"),
                          pygame.image.load(f"game/images/{gamemode}/board/board-light.png")]

        self.target_position = ()
        self.target_img = pygame.transform.scale(
            pygame.image.load(f"game/images/{gamemode}/board/target.png"), (self.size_squares_pixels, self.size_squares_pixels)
        )

    def create_board(self, screen):
        self.board_img = [pygame.transform.scale(self.board_img[0], (self.size_squares_pixels, self.size_squares_pixels)),
                          pygame.transform.scale(self.board_img[1], (self.size_squares_pixels, self.size_squares_pixels))]

        initial_position = self.board_position
        position = [self.board_position[0], self.board_position[1]]

        # define as casas do tabuleiro
        img = 0
        for x in range(0, self.size_board_squares):
            for y in range(0, self.size_board_squares):
                screen.blit(self.board_img[img % 2], position)
                img += 1
                position[0] += self.size_squares_pixels

            img += 1
            position[0] = initial_position[0]
            position[1] += self.size_squares_pixels
        pygame.display.update()

    def create_target(self, screen, player_positions=[], change=False):
        # Verifica se é necessário mudar a posição do alvo
        if change:
            while True:
                self.target_position = (randint(0, self.size_board_squares-1), randint(0, self.size_board_squares-1))
                if self.target_position not in player_positions:
                    break

        # mostra na tela o alto na nova posição
        screen.blit(self.target_img, (Game.convert(to_pixels=True,
                                                   square=self.target_position,
                                                   initial_position_board=board.board_position,
                                                   size_board_squares=board.size_board_squares,
                                                   size_board_pixels=board.size_board_pixels
                                                   )))
        pygame.display.update()
        return self.target_position


# initialize game
def run_game(gamemode):
    global screen, board

    # Variaveis iniciais
    direction = 'UP'

    game = Game(gamemode=gamemode)
    board = Board(gamemode=gamemode)
    player = Player(gamemode=gamemode)

    screen = game.create_window(window_size=(400, 500))
    screen.fill("#A9A9A9")
    board.create_board(screen=screen)
    board.create_target(screen=screen, change=True)

    game.create_text(text='SNAKE GAME', font=('mvboli', 35, (0, 0, 0)), position=(65, 5))

    clock = 24  # Essa variavel é usada como contador para determinar a movimentação do player.
    while True:
        pygame.time.wait(20)
        clock += 1

        game.lost(player)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:

                key = pygame.key.get_pressed().index(1)
                if key == 82:
                    direction = 'UP'
                elif key == 81:
                    direction = 'DOWN'
                elif key == 79:
                    direction = 'RIGHT'
                elif key == 80:
                    direction = 'LEFT'

        if gamemode == 'correios':
            if clock > 90:
                clock = 0
                player_positions = player.move(board=board, direction=direction)
                board.create_target(screen=screen, change=False, player_positions=player_positions)
                pygame.display.update()
        else:
            if clock > 15:
                clock = 0
                player_positions = player.move(board=board, direction=direction)
                board.create_target(screen=screen, change=False, player_positions=player_positions)
                pygame.display.update()

        if game.lost(player):
            pygame.time.wait(500)
            screen.fill('#000000')
            game.create_text('GAME OVER', (68, 25), ('rubik', 45, (200, 200, 200)))
            screen.blit(player.lost_img, (25, 100))
            pygame.display.update()
            pygame.time.wait(3000)
            return False
