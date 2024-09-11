import pygame

WINDOW_NAME = "Mid-autumn festival"
GAME_TITLE = WINDOW_NAME

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 700

FPS = 90
DRAW_FPS = True

# sizes
BUTTONS_SIZES = (240, 90)
HAND_SIZE = 200
HAND_HITBOX_SIZE = (60, 80)
MOONCAKE_SIZES = (50, 38)
MOONCAKE_SIZE_RANDOMIZE = (1,2) # for each new mosquito, it will multiply the size with an random value beteewn X and Y
RABBIT_SIZES = (50, 50)
RABBIT_SIZE_RANDOMIZE = (2.5, 3)

# drawing
DRAW_HITBOX = False # will draw all the hitbox

# animation
ANIMATION_SPEED = 0.08 # the frame of the moon cakes will change every X sec

# difficulty
GAME_DURATION = 30 # the game will last X sec
MOONCAKE_SPAWN_TIME = 1
MOONCAKE_MOVE_SPEED = {"min": 1, "max": 5}
RABBIT_PENALITY = 1 # will remove X of the score of the player (if he kills a rabbit)

# colors
COLORS = {"title": (250, 137, 56), "score": (38, 61, 39), "timer": (38, 61, 39),
            "buttons": {"default": (56, 67, 209), "second":  (87, 99, 255),
                        "text": (255, 255, 255), "shadow": (46, 54, 163)}} # second is the color when the mouse is on the button

# sounds / music
MUSIC_VOLUME = 0.4 # value between 0 and 1
SOUNDS_VOLUME = 1

# fonts
pygame.font.init()
FONTS = {}
FONTS["small"] = pygame.font.Font(None, 40)
FONTS["medium"] = pygame.font.Font(None, 72)
FONTS["big"] = pygame.font.Font(None, 120)
