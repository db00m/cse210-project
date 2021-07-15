from core.action import Action
import arcade

class DrawView(Action):
	
	def __init__(self, engine):
		super().__init__(engine)
		
	def execute(self, cast, cue, callback):
		for message in cast.get_actors("message"):
			message.draw()
			