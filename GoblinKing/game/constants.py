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
GEM_TARGET = 20
COMPLETION_SCORE = 500
TIME_REDUCE = 30
SCORE_DECREASE = 50


# ITEM CONSTANTS:
SCALE = 0.2
ITEMS = 5
GEM = []
GEM.append(arcade.load_texture("local_resources/stopwatch3.png"))
GEM.append(arcade.load_texture("local_resources/yellow.png"))
GEM.append(arcade.load_texture("local_resources/green.png"))
GEM.append(arcade.load_texture("local_resources/blue.png"))
GEM.append(arcade.load_texture("local_resources/red.png"))
FIRE = arcade.load_texture("local_resources/fire_new.png")
WATER = arcade.load_texture("local_resources/water2.png")
WATER_SCALE = 0.2
ITEM_CONSTANT = 128 * SCALE



# MISC:
WATER_SPRAY = arcade.load_texture("local_resources/water_spray.png")
HEART_FULL = arcade.load_texture("local_resources/heart_full.png")
HEART_EMPTY = arcade.load_texture("local_resources/heart_empty.png")


# SOUNDS:
COMPLETE_SOUND = arcade.load_sound(":resources:sounds/upgrade5.wav")
UNDERSCORE = arcade.load_sound("local_resources/underscore2.mp3")
HIT_SOUND = arcade.load_sound("local_resources/hit.wav")
COLLECT_WATER = arcade.load_sound("local_resources/collect_water.wav")
SPLASH_SOUND = arcade.load_sound("local_resources/water_splash.wav")

#PLAYER CONSTANTS
PLAYER_JUMP_SPEED = 15
PLAYER_ANIMATION_RATE = 3
PLAYER_PATH = "local_resources/player.png"
PLAYER_IDLE = arcade.load_texture(f"{PLAYER_PATH}")
