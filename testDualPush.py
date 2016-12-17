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
lo.addRead(["BUTTON9", "BUTTON10"])
lo.addActionIf(["BUTTON9", "BUTTON10"], "dualPush", "active", "LED12")
fo.write(str(lo.arduino()))

# Close opend file
fo.close()
