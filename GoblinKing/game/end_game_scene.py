#!/usr/bin/env python3

from core.cast import Cast
from core.cue import Cue
from core.scene import Scene
from core.script import Script
from game.draw_view import DrawView
from game import constants
import arcade
import random


class EndGameScene(Scene):
	
	def __init__(self, score, state="lose"):
		cast = Cast()
		

		
		message = arcade.Sprite()
		message.center_y = constants.SCREEN_HEIGHT / 2
		message.center_x = constants.SCREEN_WIDTH / 2
		if state == "lose":
			message.texture = arcade.load_texture("local_resources/game_over.png")
		elif state == "win":
			message.texture = arcade.load_texture("local_resources/you_win.png")
			
			
		
		
		cast.add_actor("message", message)
		cast.add_actor("score", score)
		
		# create the script
		draw_view = DrawView(None)
		
		
		script = Script()
		script.add_action(Cue.ON_DRAW, draw_view)
		
		
		
		# set the scene
		self.set_cast(cast)
		self.set_script(script)
	

		


		
	
	
	
	