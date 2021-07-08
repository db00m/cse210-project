from core.cast import Cast
from core.cue import Cue
from core.scene import Scene
from core.script import Script
from game.player import Player
from game.timer import Timer
from game.score import Score
from game.handle_collisions_action import HandleCollisionsAction
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.move_actors_action import MoveActorsAction
from game.maze import Maze
from game import constants
import arcade


class GameScene(Scene):

    def __init__(self):
        
        # create the cast
        player = Player()
        maze = Maze(constants.MAZE_HEIGHT,constants.MAZE_WIDTH)
        cast = Cast()
        timer = Timer()
        score = Score()
        
        cast.add_actor("walls", maze)
        cast.add_actor("player", player)
        cast.add_actor("timer", timer)
        cast.add_actor("score", score)
        
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