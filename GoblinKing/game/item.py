from core.actor import Actor

class Item(Actor):
	
	def __init__(self):
		super().__init__()
		self.scale = 0.5
		self._value = 0

		
		
	def set_scale(self, scale):
		self.scale = scale
		
		
	def set_value(self, value):
		self._value = value

	def set_texture(self, texture):
		self.texture = texture
		
	def get_value(self):
		return self._value
	