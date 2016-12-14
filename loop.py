class loop :

	def __init__(self) :
		self.m_contentString = ""
		self.m_resString = "void loop() {\n" + self.m_contentString + " }"

	def addRead(self, p_composantString) :
		self.m_contentString += "\tint reading" + p_composantString + " = digitalRead(" + p_composantString +")\n"

	def addActionIf(self, p_composantInputString, p_ifState, p_action, p_composantOutputString) :
		if (p_ifState == "push") :
			self.m_contentString += "\tif (reading" + p_composantInputString + " == HIGH && prev" + \
				p_composantInputString + " == LOW) {\n"
		elif (p_ifState == "release") :
			self.m_contentString += "\tif (reading" + p_composantInputString + " == LOW && prev" + \
				p_composantInputString + " == HIGH) {\n"
		
		if (p_action == "switch") :
			self.m_contentString += "\t\tif (state" + p_composantOutputString + " == HIGH) { state" + \
			p_composantOutputString + " = LOW; } else { state" + p_composantOutputString + " = HIGH; }\n"


		self.m_contentString += "\t\tdigitalWrite(" + p_composantOutputString + ", state" + p_composantOutputString +");\n"
		self.m_contentString +="\t}\n"
		self.m_contentString += "\tprev" + p_composantInputString + " = reading" + p_composantInputString + ";\n"

		self.m_resString = "void loop() {\n " + self.m_contentString + " \n}"


	def arduino(self) :
		return self.m_resString