import Color
from Object import Object

class Food(Object):
	def __init__(self,mass,hunger,color):
		Object.__init__(self,mass=mass,color=color)
		self.setHunger(hunger)

	def __str__(self):
		return ';'.join([str(self.hunger),Object.__str__(self)])

	def setHunger(self,hunger):
		hunger=int(hunger)
		if hunger<0:
			raise ValueError('Food cannot make hungry!')
		else:
			self.hunger=hunger

class Apple(Food):
	def __init__(self,sort,mass,hunger=5,color=Color.RGBA(red=255)):
		Food.__init__(self,mass,hunger,color)
		self.setSort(sort)

	def __str__(self):
		return ';'.join([self.sort,Food.__str__(self)])

	def setSort(self,sort):
		self.sort=str(sort)
