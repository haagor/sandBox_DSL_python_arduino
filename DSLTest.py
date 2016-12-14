#!/usr/bin/python
from button import button
from led import led
from setup import setup


# Open a file
fo = open("arduino.c", "w")


def buttonM(port) :
	b = button(port)
	fo.write(b.initArdui())

def ledM(port) :
	l = led(port)
	fo.write(l.initArdui())

def loop() :
	fo.write("void loop() {\n")
	fo.write("\tint reading = digitalRead(BUTTON);\n")
	fo.write("\tif (reading == HIGH && prev == LOW) {\n")
	fo.write("\t\tif (state == HIGH) { state = LOW; } else { state = HIGH; }\n")
	fo.write("\t}")
	fo.write("\tdigitalWrite(LED, state);\n")
	fo.write("\tprev = reading;\n")
	fo.write("}\n")

b = button(9)
l = led(12)
s = setup()
s.addComposant(b)
s.addComposant(l)
fo.write(str(s.arduino()))
loop()

# Close opend file
fo.close()
