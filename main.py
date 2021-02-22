import pygame


class Game:
    def __init__(self, gamemode):
        self.gamemode = gamemode

        avaible_gamemodes = ["city"]
        if gamemode not in avaible_gamemodes:
            print('ERROR. Gamemode unavailable.\n',
                  f'Available gamemodes are: {avaible_gamemodes}')

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
        self.img_FisrtPart = {
            'RIGHT': pygame.image.load(f'images/{gamemode}/player/first_right.png'),
            'LEFT': pygame.image.load(f"images/{gamemode}/player/first_left.png"),
            'UP': pygame.image.load(f"images/{gamemode}/player/first_up.png"),
            'DOWN': pygame.image.load(f"images/{gamemode}/player/first_down.png")
        }
        self.img_MiddlePart = {
            'RIGHT': pygame.image.load(f"images/{gamemode}/player/middle_right.png"),
            'LEFT': pygame.image.load(f"images/{gamemode}/player/middle_left.png"),
            'UP': pygame.image.load(f"images/{gamemode}/player/middle_up.png"),
            'DOWN': pygame.image.load(f"images/{gamemode}/player/middle_down.png")
        }
        self.img_LatPart = {
            'RIGHT': pygame.image.load(f"images/{gamemode}/player/last_right.png"),
            'LEFT': pygame.image.load(f"images/{gamemode}/player/last_left.png"),
            'UP': pygame.image.load(f"images/{gamemode}/player/last_up.png"),
            'DOWN': pygame.image.load(f"images/{gamemode}/player/last_down.png")
        }


class Board:
    def __init__(self, gamemode):
        self.board_img = [pygame.image.load(f"images/{gamemode}/board/board-dark.png"),
                          pygame.image.load(f"images/{gamemode}/board/board-light.png")]

    def create_board(self, position, size_board_squares, screen):
        size_board_pixels = 350
        size_squares_pixels = size_board_pixels//size_board_squares

        self.board_img = [pygame.transform.scale(self.board_img[0], (size_squares_pixels, size_squares_pixels)),
                          pygame.transform.scale(self.board_img[1], (size_squares_pixels, size_squares_pixels))]

        initial_position = position
        position = [position[0], position[1]]

        img = 0

        for x in range(0, size_board_squares):
            for y in range(0, size_board_squares):

                screen.blit(self.board_img[img % 2], position)

                img += 1
                position[0] += size_squares_pixels

            img += 1

            position[0] = initial_position[0]
            position[1] += size_squares_pixels

        pygame.display.update()

        board = []
        for x in range(0, size_board_squares):
            for y in range(0, size_board_squares):
                board.append((x, y))

        return board


gamemode = "city"

game = Game(gamemode=gamemode)

screen = game.create_window(window_size=(400, 500))
board = Board(gamemode=gamemode).create_board(position=(25, 50), size_board_squares=10, screen=screen)


pygame.time.wait(10000)
