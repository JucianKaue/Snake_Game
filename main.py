import pygame


class Game:
    def __init__(self, gamemode):
        self.gamemode = gamemode

        avaible_gamemodes = ["city"]
        if gamemode not in avaible_gamemodes:
            print('ERROR. Gamemode unavailable.\n',
                  f'Available gamemodes are: {avaible_gamemodes}')

    @staticmethod
    def convert(to_pixels, square, size_board_pixels, size_board_squares, initial_position_board):
        size_squares = size_board_pixels//size_board_squares
        if to_pixels:
            return initial_position_board[0] + (size_squares * square[0]), initial_position_board[1] + (size_squares * square[1])
        else:
            return (square[0]-initial_position_board[0])//size_squares, (square[1]-initial_position_board[1])//size_squares

    @staticmethod
    def create_window(window_size=(), bg_color='000000'):
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


class Player:
    def __init__(self, gamemode):
        self.position = [5, 5]
        self.direction = 'UP'
        self.length_player = 6

        #self.list_directions = ['UP', 'UP', 'UP', 'UP']
        #self.list_positions = [self.position, [self.position[0], self.position[1]+1], [6,5], [5,6]]

        self.player = [[],[]]

        for i in range(0, self.length_player):
            print(i)
            self.player[0].append([self.position[0], self.position[1]])
            self.player[1].append(direction)

        print(self.player)

        self.size_board_pixels = 350
        self.size_board_squares = 10
        self.size_squares_pixels = self.size_board_pixels // self.size_board_squares

        self.images = {
            'First': {
                'RIGHT': pygame.transform.scale(pygame.image.load(f'images/{gamemode}/player/first/right.png'),
                                               (self.size_squares_pixels, self.size_squares_pixels)),
                'LEFT': pygame.transform.scale(pygame.image.load(f"images/{gamemode}/player/first/left.png"),
                                               (self.size_squares_pixels, self.size_squares_pixels)),
                'UP': pygame.transform.scale(pygame.image.load(f"images/{gamemode}/player/first/up.png"),
                                               (self.size_squares_pixels, self.size_squares_pixels)),
                'DOWN': pygame.transform.scale(pygame.image.load(f"images/{gamemode}/player/first/down.png"),
                                               (self.size_squares_pixels, self.size_squares_pixels))
            },
            'Middle': {
                'RIGHT': pygame.transform.scale(pygame.image.load(f"images/{gamemode}/player/middle/right.png"),
                                               (self.size_squares_pixels, self.size_squares_pixels)),
                'LEFT': pygame.transform.scale(pygame.image.load(f"images/{gamemode}/player/middle/left.png"),
                                               (self.size_squares_pixels, self.size_squares_pixels)),
                'UP': pygame.transform.scale(pygame.image.load(f"images/{gamemode}/player/middle/up.png"),
                                               (self.size_squares_pixels, self.size_squares_pixels)),
                'DOWN': pygame.transform.scale(pygame.image.load(f"images/{gamemode}/player/middle/down.png"),
                                               (self.size_squares_pixels, self.size_squares_pixels)),
                'LEFT_UP': pygame.transform.scale(pygame.image.load(f"images/{gamemode}/player/middle_curved/right-up.png"),
                                                   (self.size_squares_pixels, self.size_squares_pixels)),
                'LEFT_DOWN': pygame.transform.scale(pygame.image.load(f"images/{gamemode}/player/middle_curved/right-down.png"),
                                                   (self.size_squares_pixels, self.size_squares_pixels)),
                'RIGHT_UP': pygame.transform.scale(pygame.image.load(f"images/{gamemode}/player/middle_curved/left-up.png"),
                                                   (self.size_squares_pixels, self.size_squares_pixels)),
                'DOWN_DOWN': pygame.transform.scale(pygame.image.load(f"images/{gamemode}/player/middle_curved/left-down.png"),
                                                   (self.size_squares_pixels, self.size_squares_pixels)),
                'UP_RIGHT': pygame.transform.scale(pygame.image.load(f"images/{gamemode}/player/middle_curved/down-right.png"),
                                                   (self.size_squares_pixels, self.size_squares_pixels)),
                'UP_LEFT': pygame.transform.scale(pygame.image.load(f"images/{gamemode}/player/middle_curved/down-left.png"),
                                                   (self.size_squares_pixels, self.size_squares_pixels)),
                'DOWN_RIGHT': pygame.transform.scale(pygame.image.load(f"images/{gamemode}/player/middle_curved/up-right.png"),
                                                   (self.size_squares_pixels, self.size_squares_pixels)),
                'DOWN_LEFT': pygame.transform.scale(pygame.image.load(f"images/{gamemode}/player/middle_curved/up-left.png"),
                                                   (self.size_squares_pixels, self.size_squares_pixels))
            },
            'Last': {
                'RIGHT': pygame.transform.scale(pygame.image.load(f"images/{gamemode}/player/last/right.png"),
                                               (self.size_squares_pixels, self.size_squares_pixels)),
                'LEFT': pygame.transform.scale(pygame.image.load(f"images/{gamemode}/player/last/left.png"),
                                               (self.size_squares_pixels, self.size_squares_pixels)),
                'UP': pygame.transform.scale(pygame.image.load(f"images/{gamemode}/player/last/up.png"),
                                               (self.size_squares_pixels, self.size_squares_pixels)),
                'DOWN': pygame.transform.scale(pygame.image.load(f"images/{gamemode}/player/last/down.png"),
                                               (self.size_squares_pixels, self.size_squares_pixels))
            }
        }

    def init_player(self, board):

        position_px = Game.convert(to_pixels=True,
                                   square=self.position,
                                   initial_position_board=board.board_position,
                                   size_board_squares=board.size_board_squares,
                                   size_board_pixels=board.size_board_pixels)

    def move(self, board, direction):

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
                    print(i)
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
            return False

        # Create the player list positions
        if direction == 'UP':
            position = (self.position[0], self.position[1] - 1)
        elif direction == 'DOWN':
            position = (self.position[0], self.position[1] + 1)
        elif direction == 'RIGHT':
            position = (self.position[0] + 1, self.position[1])
        elif direction == 'LEFT':
            position = (self.position[0] - 1, self.position[1])

        self.position = position
        self.player[0] = actualize_player_positions(position, self.player[0])
        self.player[1] = actualize_player_directions(new_direction=direction,
                                                           old_direction=self.direction,
                                                           list_directions=self.player[1])
        self.direction = direction
        print(self.player)


        # Create the player list
        images_player = []
        for i in range(0, len(self.player[0])):
            if i == 0:
                images_player.append(self.images['First'][f'{self.player[1][i]}'])
            elif i == len(self.player[0])-1:
                images_player.append(self.images['Last'][f'{self.player[1][i]}'])
            else:
                images_player.append(self.images['Middle'][f'{self.player[1][i]}'])


        screen.fill('#A9A9A9')
        board.create_board(screen)

        for i in range(0, len(images_player)):
            screen.blit(images_player[i], Game.convert(to_pixels=True,
                                                    square=self.player[0][i],
                                                    initial_position_board=board.board_position,
                                                    size_board_squares=board.size_board_squares,
                                                    size_board_pixels=board.size_board_pixels
                                                    )
                        )

            pygame.display.update()


        """# atualiza a nova posição do player baseado na direção recebida
        if direction == 'UP':
            self.position = (self.position[0], self.position[1] - 1)
        elif direction == 'DOWN':
            self.position = (self.position[0], self.position[1] + 1)
        elif direction == 'RIGHT':
            self.position = (self.position[0] + 1, self.position[1])
        elif direction == 'LEFT':
            self.position = (self.position[0] - 1, self.position[1])

        position = self.position
        player = self.player_length

        # confere se o player esté dentro do tabuleiro
        if self.position[0] < 0:
            self.position = (self.size_board_squares, self.position[1])
            return
        elif self.position[1] < 0:
            self.position = (self.position[0], self.size_board_squares)
            return
        elif self.position[0] > self.size_board_squares - 1:
            self.position = (-1, self.position[1])
            return
        elif self.position[1] > self.size_board_squares - 1:
            self.position = (self.position[0], -1)
            return

        screen.fill('#A9A9A9')
        board.create_board(screen)

        self.list_positions = [position]

        # Define as imagens do player
        player_img = []
        for i in range(0, player):
            if i == 0:
                player_img.append(self.images['First'][f'{direction}'])
            elif i == player - 1:
                player_img.append(self.images['Last'][f'{direction}'])
            else:
                player_img.append(self.images['Middle'][f'{direction}'])

            # Define the position of players parts
            if i != 0:
                if direction == 'UP':
                    position = (position[0], position[1] + 1)
                    self.list_positions.append(position)
                elif direction == 'DOWN':
                    position = (position[0], position[1] - 1)
                    self.list_positions.append(position)
                elif direction == 'RIGHT':
                    position = (position[0] - 1, position[1])
                    self.list_positions.append(position)
                elif direction == 'LEFT':
                    position = (position[0] + 1, position[1])
                    self.list_positions.append(position)

            # Don't show images when the image is outside the board
            if position[0] > self.size_board_squares - 1 or position[1] > self.size_board_squares - 1:
                return
            if position[0] < 0 or position[1] < 0:
                return

            # Show the image in the screen
            screen.blit(player_img[i], Game.convert(to_pixels=True,
                                                    square=position,
                                                    initial_position_board=board.board_position,
                                                    size_board_squares=board.size_board_squares,
                                                    size_board_pixels=board.size_board_pixels
                                                    )
                        )
            pygame.display.update()
        print(self.list_positions)
        self.list_positions = []
        return direction"""


class Board:
    def __init__(self, gamemode):

        self.board_position = (25, 50)
        self.size_board_pixels = 350
        self.size_board_squares = 10
        self.size_squares_pixels = self.size_board_pixels//self.size_board_squares

        self.board_img = [pygame.image.load(f"images/{gamemode}/board/board-dark.png"),
                          pygame.image.load(f"images/{gamemode}/board/board-light.png")]

    def create_board(self, screen):

        self.board_img = [pygame.transform.scale(self.board_img[0], (self.size_squares_pixels, self.size_squares_pixels)),
                          pygame.transform.scale(self.board_img[1], (self.size_squares_pixels, self.size_squares_pixels))]

        initial_position = self.board_position
        position = [self.board_position[0], self.board_position[1]]

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

        squares_board = []
        for x in range(0, self.size_board_squares):
            for y in range(0, self.size_board_squares):
                squares_board.append((x, y))

        return squares_board


gamemode = "city"

#initialize game

# player initial variables
direction = 'UP'

game = Game(gamemode=gamemode)
screen = game.create_window(window_size=(400, 500))
board = Board(gamemode=gamemode)
player = Player(gamemode=gamemode)
clock = 24
board.create_board(screen=screen)



while True:
    pygame.time.wait(20)

    clock += 1

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

    if clock > 50:
        clock = 0
        player.move(board=board, direction=direction)


