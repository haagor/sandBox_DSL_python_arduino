#!/usr/bin/python

# Open a file
fo = open("arduino.c", "w")

def setup() :
	fo.write("void setup() {\n")
	fo.write("\tpinMode(BUTTON, INPUT);\n")
	fo.write("\tpinMode(LED, OUTPUT);\n")
	fo.write("}\n")

def button(port) :
	res = "int BUTTON = " + str(port) + ";"
	fo.write(res + "\n")

def led(port) :
	res = "int LED = " + str(port) + ";"
	fo.write(res + "\n")

def loop() :
	fo.write("void loop() {\n")
	fo.write("\tint reading = digitalRead(BUTTON);\n")
	fo.write("\tif (reading == HIGH && prev == LOW) {\n")
	fo.write("\t\tif (state == HIGH) { state = LOW; } else { state = HIGH; }\n")
	fo.write("\t}")
	fo.write("\tdigitalWrite(LED, state);\n")
	fo.write("\tprev = reading;\n")
	fo.write("}\n")

button(9)
setup()
loop()

# Close opend file
fo.close()