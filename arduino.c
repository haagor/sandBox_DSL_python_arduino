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
	if (readingBUTTON9 == HIGH && prevBUTTON9 == LOW) {
		if (stateLED12 == HIGH) { stateLED12 = LOW; } else { stateLED12 = HIGH;}}
		stateLED12 = HIGH;}
	else if (readingBUTTON9 = LOW && prevBUTTON9 == HIGH) {
		stateLED12 = LOW;}
	digitalWrite(LED12, stateLED12);
	prevBUTTON9 = readingBUTTON9;
 
}