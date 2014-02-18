from Color import RGBA

class Object(object):
	def __init__(self,mass=0,color=RGBA()):
		self.setMass(mass)
		self.setColor(color)

	def __str__(self):
		return ';'.join([str(self.mass)+'kg',str(self.color)])

	def __repr__(self):
		return str(self)

	def setMass(self,mass):
		mass=float(mass)
		if mass<0:
			raise ValueError('Object cannot have negative weight')
		else:
			self.mass=mass

	def setColor(self,color):
		if type(color)!=RGBA:
			raise ValueError()
		else:
			self.color=color
