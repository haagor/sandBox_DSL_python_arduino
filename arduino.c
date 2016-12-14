int BUTTON9 = 9;
int state9 = LOW; int prev9 = HIGH;
int LED = 12;
void setup() {
	pinMode(BUTTON, INPUT);
	pinMode(LED, OUTPUT);
}
void loop() {
	int reading = digitalRead(BUTTON);
	if (reading == HIGH && prev == LOW) {
		if (state == HIGH) { state = LOW; } else { state = HIGH; }
	}	digitalWrite(LED, state);
	prev = reading;
}
