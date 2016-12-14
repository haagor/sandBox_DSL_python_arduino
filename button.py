class button :

	def __init__(self, p) :
		self.port = p

	def initArdui(self) :
		res = "int BUTTON = " + str(self.port) + ";"
		res += "\n"
		res += "int state = LOW; int prev = HIGH;\n"
		return res