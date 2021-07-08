from core.actor import Actor

class Item(Actor):
	
	def __init__(self):
		super().__init__()
		self.scale = 0.5
		self._value = 0
		self._hazard = 0
		
		
		
		
		
	def set_value(self, value):
		self._value = value

	def set_texture(self, texture):
		self.texture = texture
		
	def get_value(self):
		return self._value
	
	def set_hazard(self, is_hazard=True):
		"""Sets the item as a hazard unless otherwise indicated"""
		self._hazard = is_hazard
		
	def is_hazard(self):
		"""Returns a bool indicating if the item is a hazard"""
		return self._hazard
	