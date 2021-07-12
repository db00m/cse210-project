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
ITEMS = 5
GEM = []
GEM.append(arcade.load_texture(":resources:images/items/gemYellow.png"))
GEM.append(arcade.load_texture(":resources:images/items/gemGreen.png"))
GEM.append(arcade.load_texture(":resources:images/items/gemRed.png"))
GEM.append(arcade.load_texture(":resources:images/items/gemBlue.png"))
#GEM.append(arcade.load_texture("local_resources/stopwatch.png"))
FIRE = arcade.load_texture("local_resources/fire.png")
WATER = arcade.load_texture("local_resources/water.png")
WATER_SCALE = 0.02
COMPLETION_SCORE = 500
SCORE_DECREASE = 50
ITEM_CONSTANT = 128 * SCALE

# ANIMAL CONSTANTS
PLAYER_JUMP_SPEED = 15
PLAYER_ANIMATION_RATE = 3
PLAYER_PATH = ":resources:images/enemies/slimeBlock.png"
PLAYER_IDLE = arcade.load_texture(f"{PLAYER_PATH}")
