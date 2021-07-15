#!/usr/bin/env python3

from core.cast import Cast
from core.cue import Cue
from core.scene import Scene
from core.script import Script
from game.draw_menu_action import DrawMenuAction
from game.menu_control_action import MenuContolAction
from game import constants
import arcade


class StartGameScene(Scene):
	
	def __init__(self):
		cast = Cast()
		
		
		
		game_title = arcade.Sprite()
		game_title.center_y = constants.SCREEN_HEIGHT / 2
		game_title.center_x = constants.SCREEN_WIDTH / 2
		#TODO: Create a game title png and load it as a texture here
			
			
			
			
		cast.add_actor("title", game_title)
		
		# create the script
		draw_menu = DrawMenuAction(None)
		menu_control = MenuContolAction(None)
		
		
		script = Script()
		script.add_action(Cue.ON_DRAW, draw_menu)
		script.add_action(Cue.ON_KEY_PRESS, menu_control)
		
		
		
		# set the scene
		self.set_cast(cast)
		self.set_script(script)
		
		
		
		
		
		
		
		
		
		

		