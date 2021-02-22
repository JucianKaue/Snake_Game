import pygame


class Game:
    def __init__(self, gamemode):
        self.gamemode = gamemode

        avaible_gamemodes = ["city"]
        if gamemode not in avaible_gamemodes:
            print('ERROR. Gamemode unavailable.\n',
                  f'Available gamemodes are: {avaible_gamemodes}')

    @staticmethod
    def create_window(window_size=(), bg_color="000000"):
        try:
            pygame.init()
        except:
            print("ERROR! It's not possible initialize module pygame.")
            return False
        try:
            if len(window_size) == 2:

                screen = pygame.display.set_mode(window_size)
                screen.fill(bg_color)

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


game = Game(gamemode="city")
game.create_window(window_size=(400, 400))
