from core.action import Action
import arcade

class DrawMenuAction(Action):
	
	def __init__(self, engine):
		super().__init__(engine)
		
	def execute(self, cast, cue, callback):
		title = cast.first_actor("title")
		arcade.draw_text("Press 'Enter' to Start", title.center_x, title.center_y, arcade.color.WHITE, 16)
		