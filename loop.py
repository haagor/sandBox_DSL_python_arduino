class loop :

	def __init__(self) :
		self.m_contentString = ""
		self.m_resString = "void loop() {\n" + self.m_contentString + " }"
		self.m_multiAction = 0

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
				p_composantInputString[1] + " == HIGH && (prev" + p_composantInputString[0] + " == LOW || prev" + \
				p_composantInputString[1] + " == LOW) {\n"

		for c_action in p_action :
			if (c_action == "switch") :
				self.m_contentString += "\t\tif (state" + p_composantOutputString + " == HIGH) { state" + \
				p_composantOutputString + " = LOW; } else { state" + p_composantOutputString + " = HIGH;}}\n"
			elif (c_action == "active") :
				self.m_contentString += "\t\tstate" + p_composantOutputString + " = HIGH;}\n"
			elif (c_action == "unactive") :
				self.m_contentString += "\t\tstate" + p_composantOutputString + " = LOW;}\n"
		
		for c_action in p_action :
			if (c_action == "active") :
				for c_composantInput in p_composantInputString :
					self.m_contentString += "\telse if (reading" + c_composantInput + " = LOW && prev" + \
						c_composantInput + " == HIGH) {\n\t\tstate" + p_composantOutputString + " = LOW;}\n"

		self.m_contentString += "\tdigitalWrite(" + p_composantOutputString + ", state" + p_composantOutputString +");\n"
		for c_composantInput in p_composantInputString : 
			self.m_contentString += "\tprev" + c_composantInput + " = reading" + c_composantInput + ";\n" 
		

		self.m_resString = "void loop() {\n " + self.m_contentString + " \n}"


	def arduino(self) :
		return self.m_resString