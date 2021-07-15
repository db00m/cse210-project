import arcade
from core.director import Director
from game import constants
from game.game_scene import GameScene


def main():
    width = constants.SCREEN_WIDTH
    height = constants.SCREEN_HEIGHT
    title = constants.SCREEN_TITLE
    game_scene = GameScene()
    director = Director(width, height, title)
    director.direct_scene(game_scene)
    arcade.run()


if __name__ == "__main__":
    main()