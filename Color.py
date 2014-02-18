def chartohex(c):
	c=int(c)
	s=hex(c)[2:]
	if len(s)<2:
		s='0'+s
	return s

class RGB(object):
	def __init__(self,red=0,green=0,blue=0):
		self.setRed(red)
		self.setGreen(green)
		self.setBlue(blue)

	def __str__(self):
		return ''.join(['#',chartohex(self.red),chartohex(self.green),chartohex(self.blue)])

	def __repr__(self):
		return str(self)

	def setRed(self,color):
		self.red=ord(chr(color))

	def setGreen(self,color):
		self.green=ord(chr(color))

	def setBlue(self,color):
		self.blue=ord(chr(color))

class RGBA(RGB):
	def __init__(self,red=0,green=0,blue=0,alpha=255):
		RGB.__init__(self,red,green,blue)
		self.setAlpha(alpha)

	def __str__(self):
		return RGB.__str__(self)+chartohex(self.alpha)

	def setAlpha(self,color):
		self.alpha=ord(chr(color))

