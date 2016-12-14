class button :

	def __init__(self, p) :
		self.port = p

	def initArdui(self) :
		res = "int BUTTON" + str(self.port) + " = " + str(self.port) + ";"
		res += "\n"
		res += "int state" + str(self.port) + " = LOW; int prev" + str(self.port) + " = HIGH;\n"
		return res