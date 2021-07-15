from core.actor import Actor
from game import constants
import arcade

class WaterSpray(Actor):
	
	def __init__(self):
		super().__init__()
		self.texture = constants.WATER_SPRAY
		self.scale = 0.005
		self._splash_time = 0
		self._grow_rate = 0.00
		
	def move(self,player):
		self.center_x = player.center_x
		self.center_y = player.center_y - 1
		if self._grow_rate > 0:
			self._splash_time += 1
			if self._splash_time > 0 and self._splash_time < 20:
				self.scale += self._grow_rate
				self._points = None
			else:
				self.scale = 0.01
		

	def splash(self):
		self._grow_rate = 0.015
		
	def stop(self):
		self.scale = 0.01
		self._grow_rate = 0.00
		self._splash_time = 0
		
	def get_type(self):
		return self._type