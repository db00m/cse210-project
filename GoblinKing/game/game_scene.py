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
import arcade
import random


class GameScene(Scene):

    def __init__(self):
        
        # create the cast
        player = Player()
        maze = Maze(constants.MAZE_HEIGHT,constants.MAZE_WIDTH)
        cast = Cast()

        # Create Items list
        items = arcade.SpriteList()
        # Add items to list and place them on the maze
        
        # For some strange reason, this function is only recognized within __init__ and cannot be made a method of GameScene.
        def place_objects(texture, type, number,scale=0.75,left=25,right=600,upper=600,lower=25):
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
                
        hazards = place_objects(constants.FIRE, "fire",3, scale=0.05, left=300,lower=300)
        waters = place_objects(
                constants.WATER, 
                "water",
                3, 
                scale=constants.WATER_SCALE, 
                right=300,
                lower=150,
                upper=450
        )


        
        timer = Timer()
        score = Score()
        
        cast.add_actor("walls", maze)
        cast.add_actor("player", player)
        cast.add_actor("timer", timer)
        cast.add_actor("score", score)
        cast.add_actor("items", items)
        cast.add_actor("items", hazards)
        cast.add_actor("items", waters)
                
        
        engine = arcade.PhysicsEngineSimple(player, maze)

        # create the script
        draw_actors_action = DrawActorsAction(engine)
        control_actors_action = ControlActorsAction(engine)
        move_actors_action = MoveActorsAction(engine)
        handel_collisions = HandleCollisionsAction(engine)

        script = Script()
        script.add_action(Cue.ON_DRAW, draw_actors_action)
        script.add_action(Cue.ON_KEY_PRESS, control_actors_action)
        script.add_action(Cue.ON_KEY_RELEASE, control_actors_action)
        script.add_action(Cue.ON_UPDATE, move_actors_action)
        script.add_action(Cue.ON_UPDATE, handel_collisions)
        
        
        # set the scene
        self.set_cast(cast)
        self.set_script(script)
        
        
        

                