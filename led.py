class led :

	def __init__(self, p_port) :
		self.m_port = p_port
		self.m_portString = "int LED" + str(self.m_port) + " = " + str(self.m_port) + ";"
		self.m_stateString = "int state" + str(self.m_port) + " = LOW; int prev" + str(self.m_port) + " = HIGH;\n"
		self.m_pinModeString = "\tpinMode(LED" + str(self.m_port) + ", OUTPUT);\n"

	def arduino(self) :
		res = "int LED" + str(self.m_port) + " = " + str(self.m_port) + ";"
		res += "\n"
		res += "int state" + str(self.m_port) + " = LOW; int prev" + str(self.m_port) + " = HIGH;\n"
		return res