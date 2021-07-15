from core.actor import Actor
from game import constants

class Lives(Actor):
	
	def __init__(self):
		super().__init__()
		self.scale = 2
		height = constants.SCREEN_HEIGHT
		width = constants.SCREEN_WIDTH
		self.center_x = width - 20
		self.center_y = 16
		self.set_texture()
		
	def set_texture(self):
		self.texture = constants.HEART_FULL
		
	def lose_heart(self):
		self.texture = constants.HEART_EMPTY
		self.draw()
	
		