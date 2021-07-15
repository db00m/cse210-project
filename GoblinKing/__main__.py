import arcade
from core.director import Director
from game import constants
from game.start_game_scene import StartGameScene

def main():
    width = constants.SCREEN_WIDTH
    height = constants.SCREEN_HEIGHT
    title = constants.SCREEN_TITLE
    start_scene = StartGameScene()
    director = Director(width, height, title)
    director.direct_scene(start_scene)
    arcade.run()


if __name__ == "__main__":
    main()