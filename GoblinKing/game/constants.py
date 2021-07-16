import arcade

# GAME CONSTANTS
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 607
SCREEN_TITLE = "Realm of the King"
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2
MAZE_WIDTH = 20
MAZE_HEIGHT = 20
MOVE_SPEED = 2
RIGHT = "r"
LEFT = "l"
UP = "u"
DOWN = "d"
SCALE = 0.2
ITEMS = 5
GEM = []
GEM.append(arcade.load_texture(":resources:images/items/gemYellow.png"))
GEM.append(arcade.load_texture(":resources:images/items/gemGreen.png"))
GEM.append(arcade.load_texture(":resources:images/items/gemBlue.png"))
GEM.append(arcade.load_texture(":resources:images/items/gemRed.png"))
GEM.append(arcade.load_texture("local_resources/stopwatch3.png"))
FIRE = arcade.load_texture("local_resources/fire.png")
WATER = arcade.load_texture("local_resources/water2.png")
WATER_SPRAY = arcade.load_texture("local_resources/water_spray.png")
HEART_FULL = arcade.load_texture("local_resources/heart_full.png")
HEART_EMPTY = arcade.load_texture("local_resources/heart_empty.png")
WATER_SCALE = 0.2
COMPLETION_SCORE = 500
TIME_REDUCE = 30
SCORE_DECREASE = 50
ITEM_CONSTANT = 128 * SCALE
GEM_TARGET = 20

# ANIMAL CONSTANTS
PLAYER_JUMP_SPEED = 15
PLAYER_ANIMATION_RATE = 3
PLAYER_PATH = "local_resources/player.png"
PLAYER_IDLE = arcade.load_texture(f"{PLAYER_PATH}")
