class loop :

	def __init__(self) :
		self.m_contentString = ""
		self.m_resString = "void loop() {\n" + self.m_contentString + " }"

	def addRead(self, p_composantString) :
		for c_composant in p_composantString :
			self.m_contentString += "\tint reading" + c_composant + " = digitalRead(" + c_composant +")\n"

	def addActionIf(self, p_composantInputString, p_ifState, p_action, p_composantOutputString) :
		if (p_ifState == "push") :
			self.m_contentString += "\tif (reading" + p_composantInputString[0] + " == HIGH && prev" + \
				p_composantInputString[0] + " == LOW) {\n"
		elif (p_ifState == "release") :
			self.m_contentString += "\tif (reading" + p_composantInputString[0] + " == LOW && prev" + \
				p_composantInputString[0] + " == HIGH) {\n"
		elif (p_ifState == "pushTT") :
			self.m_contentString += "\tif (reading" + p_composantInputString[0] + " = HIGH && prev" + \
				p_composantInputString[0] + " == LOW) {\n"
		elif (p_ifState == "dualPush") :
			if (len(p_composantInputString) != 2) : 
				return "error"
			self.m_contentString += "\tif (reading" + p_composantInputString[0] + " == HIGH && reading" + \
				p_composantInputString[1] + " == HIGH) {\n"

		
		if (p_action == "switch") :
			self.m_contentString += "\t\tif (state" + p_composantOutputString + " == HIGH) { state" + \
			p_composantOutputString + " = LOW; }\n\t\telse { state" + p_composantOutputString + " = HIGH;\n"
		elif (p_action == "active") :
			self.m_contentString += "\t\tstate" + p_composantOutputString + " = HIGH;\n"
		
		self.m_contentString += "\t\tdigitalWrite(" + p_composantOutputString + ", state" + p_composantOutputString +");\n\t}\n"


		if (p_action == "active") :
			self.m_contentString += "\tif (reading" + p_composantInputString[0] + " = LOW && prev" + \
				p_composantInputString[0] + " == HIGH) {\n\t\tstate" + p_composantOutputString + " = LOW;" \
			+ "\n\t\tdigitalWrite(" + p_composantOutputString + ", state" + p_composantOutputString +");\n"


		self.m_contentString +="\t}\n"
		if (p_ifState == "push" or p_ifState == "release") :
			self.m_contentString += "\tprev" + p_composantInputString[0] + " = reading" + p_composantInputString[0] + ";\n" 
		self.m_resString = "void loop() {\n " + self.m_contentString + " \n}"


	def arduino(self) :
		return self.m_resString