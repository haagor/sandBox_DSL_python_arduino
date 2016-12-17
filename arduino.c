int BUTTON9 = 9;
int stateBUTTON9 = LOW; int prevBUTTON9 = HIGH;

int LED12 = 12;
int stateLED12 = LOW; int prevLED12 = HIGH;

void setup() {
	pinMode(BUTTON9, INPUT);
	pinMode(LED12, OUTPUT);
}
void loop() {
 	int readingBUTTON9 = digitalRead(BUTTON9)
	if (readingBUTTON9 = HIGH) {
		stateLED12 = HIGH; }
		digitalWrite(LED12, stateLED12);
	else { stateLED12 = LOW; }
	}
	prevBUTTON9 = readingBUTTON9;
 
}