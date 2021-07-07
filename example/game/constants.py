import arcade

# GAME CONSTANTS
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2
GRAVITY = 0.5
MAZE_WIDTH = 30
MAZE_HEIGHT = 30
MOVE_SPEED = 3
RIGHT = "r"
LEFT = "l"
UP = "u"
DOWN = "d"
SCALE = 0.5

# ANIMAL CONSTANTS
PLAYER_JUMP_SPEED = 15
PLAYER_ANIMATION_RATE = 3
PLAYER_PATH = ":resources:images/animated_characters/female_person"
PLAYER_FALLING = arcade.load_texture(f"{PLAYER_PATH}/femalePerson_fall.png")
PLAYER_IDLE = arcade.load_texture(f"{PLAYER_PATH}/femalePerson_idle.png")
PLAYER_JUMPING = arcade.load_texture(f"{PLAYER_PATH}/femalePerson_jump.png")
PLAYER_WALKING = [None] * 8 
PLAYER_WALKING[0] = arcade.load_texture(f"{PLAYER_PATH}/femalePerson_walk0.png")
PLAYER_WALKING[1] = arcade.load_texture(f"{PLAYER_PATH}/femalePerson_walk1.png")
PLAYER_WALKING[2] = arcade.load_texture(f"{PLAYER_PATH}/femalePerson_walk2.png")
PLAYER_WALKING[3] = arcade.load_texture(f"{PLAYER_PATH}/femalePerson_walk3.png")
PLAYER_WALKING[4] = arcade.load_texture(f"{PLAYER_PATH}/femalePerson_walk4.png")
PLAYER_WALKING[5] = arcade.load_texture(f"{PLAYER_PATH}/femalePerson_walk5.png")
PLAYER_WALKING[6] = arcade.load_texture(f"{PLAYER_PATH}/femalePerson_walk6.png")
PLAYER_WALKING[7] = arcade.load_texture(f"{PLAYER_PATH}/femalePerson_walk7.png")

# GROUND CONSTANTS

GROUND_MOVE_SPEED = -8
GROUND_PATH = ":resources:images/tiles"
GROUND_GRASS = arcade.load_texture(f"{GROUND_PATH}/grass.png")