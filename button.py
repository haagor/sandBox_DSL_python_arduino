class button :

	def __init__(self, p_port) :
		self.m_port = p_port
		self.m_portString = "int BUTTON" + str(self.m_port) + " = " + str(self.m_port) + ";"
		self.m_stateString = "int state" + str(self.m_port) + " = LOW; int prev" + str(self.m_port) + " = HIGH;\n"
		self.m_pinModeString = "\tpinMode(BUTTON" + str(self.m_port) + ", INPUT);\n"

	def arduino(self) :
		res = "int BUTTON" + str(self.m_port) + " = " + str(self.m_port) + ";"
		res += "\n"
		res += "int state" + str(self.m_port) + " = LOW; int prev" + str(self.m_port) + " = HIGH;\n"
		return res