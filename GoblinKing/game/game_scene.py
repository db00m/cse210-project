from core.cast import Cast
from core.cue import Cue
from core.scene import Scene
from core.script import Script
from game.player import Player
from game.handle_collisions_action import HandleCollisionsAction
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.move_actors_action import MoveActorsAction
from game.maze import Maze
from game.item import Item
from game import constants
import arcade
import random


class GameScene(Scene):

    def __init__(self):
        
        # create the cast
        player = Player()
        maze = Maze(constants.MAZE_HEIGHT,constants.MAZE_WIDTH)
        cast = Cast()
        items = arcade.SpriteList()
        for _ in range(constants.ITEMS):
                item = Item()
                placed = False
                item.set_texture(constants.GEM[0]) # In the future their will be diffrent types of gems
                while not placed:
                        # Randomly position
                        item.center_x = random.randrange(constants.MAZE_WIDTH * 128 * constants.SCALE)
                        item.center_y = random.randrange(constants.MAZE_HEIGHT * 128 * constants.SCALE)
                        
                        # Are we in a wall?
                        walls_hit = arcade.check_for_collision_with_list(item, maze)
                        if len(walls_hit) == 0:
                                # Not in a wall! Success!
                                placed = True
                items.append(item)
        
        cast.add_actor("walls", maze)
        cast.add_actor("player", player)
        cast.add_actor("items", items)
        
        engine = arcade.PhysicsEngineSimple(player, maze)

        # create the script
        draw_actors_action = DrawActorsAction(engine)
        control_actors_action = ControlActorsAction(engine)
        move_actors_action = MoveActorsAction(engine)

        script = Script()
        script.add_action(Cue.ON_DRAW, draw_actors_action)
        script.add_action(Cue.ON_KEY_PRESS, control_actors_action)
        script.add_action(Cue.ON_KEY_RELEASE, control_actors_action)
        script.add_action(Cue.ON_UPDATE, move_actors_action)
        
        
        # set the scene
        self.set_cast(cast)
        self.set_script(script)