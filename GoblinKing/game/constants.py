import arcade

# GAME CONSTANTS
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2
MAZE_WIDTH = 25
MAZE_HEIGHT = 25
MOVE_SPEED = 3
RIGHT = "r"
LEFT = "l"
UP = "u"
DOWN = "d"
SCALE = 0.2

# ANIMAL CONSTANTS
PLAYER_JUMP_SPEED = 15
PLAYER_ANIMATION_RATE = 3
PLAYER_PATH = ":resources:images/enemies/slimeBlock.png"
PLAYER_IDLE = arcade.load_texture(f"{PLAYER_PATH}")
