from core.cast import Cast
from core.cue import Cue
from core.scene import Scene
from core.script import Script
from game.player import Player
from game.ground import Ground
from game.instructions import Instruction
from game.handle_collisions_action import HandleCollisionsAction
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.move_actors_action import MoveActorsAction
from game.maze import Maze
import arcade


class GameScene(Scene):

    def __init__(self):
        
        # create the cast
        player = Player()
        maze = Maze()
        cast = Cast()
        
        
        cast.add_actor("Walls", maze)
        
        engine = arcade.PhysicsEngineSimple(player, maze)

        # create the script
        move_actors_action = MoveActorsAction(engine)
        handle_collisions_action = HandleCollisionsAction(engine)
        draw_actors_action = DrawActorsAction(engine)

        script = Script()
        script.add_action(Cue.ON_UPDATE, move_actors_action)
        script.add_action(Cue.ON_UPDATE, handle_collisions_action)
        script.add_action(Cue.ON_DRAW, draw_actors_action)
        
        # set the scene
        self.set_cast(cast)
        self.set_script(script)