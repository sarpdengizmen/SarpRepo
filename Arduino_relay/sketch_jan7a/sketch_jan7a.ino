const byte ledPin = 13;
const byte interruptPin = 2;
volatile byte state = LOW;
bool val;
const byte switchpin = 3;
void setup() {
  pinMode(interruptPin, INPUT);
  pinMode(switchpin, OUTPUT);
  Serial.begin(9600);   
}

void loop() {
  val = digitalRead(interruptPin);
  Serial.println(val);
  if (val == 1) {
    digitalWrite(switchpin, HIGH);
  } else {
    digitalWrite(switchpin, LOW);
  }
  
}

void blink() {
  state = !state;
}