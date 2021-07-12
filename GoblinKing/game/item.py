from core.actor import Actor

class Item(Actor):
	
	def __init__(self):
		super().__init__()
		self.scale = 0.5
		self._value = 0
		self._type = "item"
		self.is_static = True
		
	def set_scale(self, scale):
		self.scale = scale
		
		
	def set_value(self, value):
		self._value = value

	def set_texture(self, texture):
		self.texture = texture
		
	def get_value(self):
		return self._value
	
	def set_type(self,type):
		self._type = type
	
	def get_type(self):
		return self._type
	