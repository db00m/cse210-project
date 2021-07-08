import arcade

# GAME CONSTANTS
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2
MAZE_WIDTH = 20
MAZE_HEIGHT = 20
MOVE_SPEED = 3
RIGHT = "r"
LEFT = "l"
UP = "u"
DOWN = "d"
SCALE = 0.2
ITEMS = 10
GEM = []
GEM.append(arcade.load_texture(":resources:images/items/gemYellow.png"))
COMPLETION_SCORE = 500
SCORE_DECREASE = 50

# ANIMAL CONSTANTS
PLAYER_JUMP_SPEED = 15
PLAYER_ANIMATION_RATE = 3
PLAYER_PATH = ":resources:images/enemies/slimeBlock.png"
PLAYER_IDLE = arcade.load_texture(f"{PLAYER_PATH}")
