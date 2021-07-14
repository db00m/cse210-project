#!/usr/bin/env python3

import arcade
from core.action import Action
from game import constants
from core.cue import Cue


class CheckConditionsAction(Action):
	
	def __init__(self, engine):
		super().__init__(engine)
		
	def execute(self, cast, cue, callback):
		cue_info = cue.get_info()
		player = cast.first_actor("player")
		timer = cast.first_actor("timer")
		score = cast.first_actor("score")
		if player.check_win():
			score.calculate_time_score(timer.elapsed_time)
			callback.get_scene().set_scene()
				
				
