class setup :

	def __init__(self) :
		self.m_vars = ""
		self.m_pinModes = ""
		self.m_resString = str(self.m_vars) + "void setup() {\n" + str(self.m_pinModes) + "\n}"

	def addComposant(self, p_composant) :
		self.m_vars += p_composant.m_portString + "\n" + p_composant.m_stateString + "\n"
		self.m_pinModes += str(p_composant.m_pinModeString)
		self.m_resString = str(self.m_vars) + "void setup() {\n" + str(self.m_pinModes) + "}\n"

	def arduino(self) :
		return self.m_resString