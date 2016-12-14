#!/usr/bin/python
from button import button
from led import led
from setup import setup
from loop import loop


# Open a file
fo = open("arduino.c", "w")


b = button(9)
le = led(12)
s = setup()
s.addComposant(b)
s.addComposant(le)
fo.write(str(s.arduino()))

lo = loop()
lo.addRead("BUTTON9")
lo.addActionIf("BUTTON9", "push", "switch", "LED12")
fo.write(str(lo.arduino()))

# Close opend file
fo.close()
