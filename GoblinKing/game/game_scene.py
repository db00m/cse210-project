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
from game.item import Item
from game import constants
from game.check_conditions_action import CheckConditionsAction
from game.water_spray import WaterSpray
from game.gem_count import GemCount
from game.lives import Lives
import arcade
import random


class GameScene(Scene):

    def __init__(self):
        self._score = Score()
        self._gem_count = GemCount()
        water_spray = WaterSpray()
        self._player = Player(water_spray)
                
                
        self.set_scene()
        
                
    def set_scene(self):
        
        # create the cast
        water_list = arcade.SpriteList()
        maze = Maze(constants.MAZE_HEIGHT,constants.MAZE_WIDTH)
        timer = Timer()
        self._player.reset()
        
                

        # Create Items list
        items = arcade.SpriteList()
        # Add items to list and place them on the maze
        
        # For some strange reason, this function is only recognized within __init__ and cannot be made a method of GameScene.
        def place_objects(texture, type, number,scale=0.75,left=0,right=constants.SCREEN_WIDTH,upper=constants.SCREEN_HEIGHT,lower=0):
                """ This function places items and random locations on the map.
                
                args:
                        texture: A loaded sprite texture
                        number(Int): Number of items to be placed
                        scale(Float): Sprite scale number
                        left(Int):  The left boundry for placing items (must be > right)
                        right(Int): The right boundry for placing items
                        upper(Int): The upper boundry for placing items
                        lower(Int): The lower boundry for placing items
                return -> (arcade.SprtieList): a list of the placed items
                """
                
                objects = arcade.SpriteList()
                # Add items to list and place them on the maze
                for _ in range(number):
                        object = Item()
                        object.set_scale(scale)
                        object.set_type(type)
                        placed = False
                        object.set_texture(texture) # In the future their will be diffrent types of gems/items
                        while not placed:
                                # Randomly position
                                object.center_x = random.randrange(left, right)
                                object.center_y = random.randrange(lower, upper)
                                
                                # Are we in a wall?
                                walls_hit = arcade.check_for_collision_with_list(object, maze)
                                self_hit = arcade.check_for_collision_with_list(object, objects)
                                if len(walls_hit) == 0:
                                        # Not in a wall! Success!
                                        if len(self_hit) == 0:
                                                placed = True
                        objects.append(object)
                return objects
        
        
        # TODO Once we have the Gems figured out, this code should disapear and place_ojects() should be called.
        for _ in range(constants.ITEMS):
                item = Item()
                gem_or_time = random.randint(1, 3)
                if gem_or_time == 3:
                        item_type = 5
                        item._value = 0
                        item.scale = 0.02
                else:
                        item_type = random.randint(1, 4)
                        item._value = item_type * 10

                item.set_texture(constants.GEM[item_type - 1])
                placed = False
                while not placed:
                        # Randomly position
                        item.center_x = random.randrange((constants.MAZE_WIDTH) * constants.ITEM_CONSTANT)
                        item.center_y = random.randrange((constants.MAZE_HEIGHT) * constants.ITEM_CONSTANT)
                        
                        # Are we in a wall?
                        walls_hit = arcade.check_for_collision_with_list(item, maze)
                        if len(walls_hit) == 0:
                                # Not in a wall! Success!
                                placed = True
                items.append(item)

        #Place fire:
        hazards = place_objects(
                constants.FIRE, 
                "fire",
                5, 
                scale=0.05,
                left=400,
                lower=400
        )
        #Place water:
        waters = place_objects(
                constants.WATER, 
                "water",
                5, 
                scale=constants.WATER_SCALE, 
                right=300,
                upper=200
        )
        
                
        self._cast = Cast()
                
        self._cast.add_actor("timer", timer)
        self._cast.add_actor("score", self._score)
        self._cast.add_actor("gem count", self._gem_count)
        # Fill the cast
        
        self._cast.add_actor("walls", maze)
        self._cast.add_actor("player", self._player)

        self._cast.add_actor("items", items)
        self._cast.add_actor("items", hazards)
        self._cast.add_actor("items", waters)
        

        for i in range(0,3):
                life = Lives()
                life.center_x -= i * 32
                self._cast.add_actor("lives", life)
                
        
        engine = arcade.PhysicsEngineSimple(self._player, maze)

        # create the script
        draw_actors_action = DrawActorsAction(engine)
        control_actors_action = ControlActorsAction(engine)
        move_actors_action = MoveActorsAction(engine)
        handel_collisions = HandleCollisionsAction(engine)
        check_conditions = CheckConditionsAction(engine)

        script = Script()
        script.add_action(Cue.ON_DRAW, draw_actors_action)
        script.add_action(Cue.ON_KEY_PRESS, control_actors_action)
        script.add_action(Cue.ON_KEY_RELEASE, control_actors_action)
        script.add_action(Cue.ON_UPDATE, move_actors_action)
        script.add_action(Cue.ON_UPDATE, handel_collisions)
        script.add_action(Cue.ON_UPDATE, check_conditions)
        
        
        # set the scene
        self.set_cast(self._cast)
        self.set_script(script)
        
        
        

                