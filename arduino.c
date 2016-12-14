int BUTTON9 = 9;
int state9 = LOW; int prev9 = HIGH;

int LED12 = 12;
int state12 = LOW; int prev12 = HIGH;

void setup() {
	pinMode(LED9, INPUT);
	pinMode(LED12, OUTPUT);

}void loop() {
	int reading = digitalRead(BUTTON);
	if (reading == HIGH && prev == LOW) {
		if (state == HIGH) { state = LOW; } else { state = HIGH; }
	}	digitalWrite(LED, state);
	prev = reading;
}
