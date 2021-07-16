from core.action import Action
import arcade

class DrawView(Action):
	
	def __init__(self, engine):
		super().__init__(engine)
		
	def execute(self, cast, cue, callback):
		x = 0
		y = 0
		for message in cast.get_actors("message"):
			x = message.center_x 
			y = message.center_y
			message.draw()
		
		score = cast.first_actor("score")
		output = f"Final Score: {score}"
		arcade.draw_text(output, x-80, 80, arcade.color.WHITE, 16)