#!/usr/bin/env python3

import arcade
from core.action import Action
from game import constants
from core.cue import Cue
from game.end_game_scene import EndGameScene


class CheckConditionsAction(Action):
	
	def __init__(self, engine):
		super().__init__(engine)
		
	def execute(self, cast, cue, callback):
		cue_info = cue.get_info()
		player = cast.first_actor("player")
		if player.check_complete():
			if player.check_win():
				callback.on_scene_finished(EndGameScene(state="win"))
			else:
				callback.get_scene().set_scene()
		elif player.check_death():
			callback.on_scene_finished(EndGameScene(state="lose"))
				
				
			