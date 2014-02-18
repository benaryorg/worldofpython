import Color
from Object import Object

class Food(Object):
	def __init__(self,mass,hunger,color):
		Object.__init__(self,mass=mass,color=color)
		self.setHunger(hunger)

	def __str__(self):
		return ';'.join([str(self.hunger),Object.__str__(self)])

	def setHunger(self,hunger):
		if hunger==None:
			hunger=self.mass*50
		hunger=int(hunger)
		if hunger<0:
			raise ValueError('Food cannot make hungry!')
		else:
			self.hunger=hunger

	def eat(self):
		self.setMass(0)
		hunger=self.hunger
		self.setHunger(None)
		return hunger

class Fruit(Food):
	def __init__(self,mass,color,hunger=None):
		Food.__init__(self,mass,hunger,color)

	def __str__(self):
		return ';'.join([self.__class__.__name__,Food.__str__(self)])

