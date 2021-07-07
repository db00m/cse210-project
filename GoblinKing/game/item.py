from core.actor import Actor

class Item(Actor):
	
	def __init__(self):
		super().__init__()
		self.scale = 0.2
		self._value = 0
		self.scale = 0.5
		
	def set_value(self, value):
		self._value = value

	def set_texture(self, texture):
		self.texture = texture
		
	def get_value(self):
		return self._value