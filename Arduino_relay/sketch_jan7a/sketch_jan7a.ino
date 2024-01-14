const byte interruptPin = 2;
bool val;
const byte switchpin = 3;
volatile int rev = 0;
unsigned long timer = 0;
unsigned long time_taken = 0;
long rpm = 0;
bool flag = 0;

void setup() {
  pinMode(interruptPin, INPUT);
  pinMode(switchpin, OUTPUT);
  Serial.begin(9600);   
  attachInterrupt(digitalPinToInterrupt(interruptPin), revcounter, RISING);
  timer = millis();
}

void loop() {
  if (rev >= 5) {
    // disable interrupts
    detachInterrupt(digitalPinToInterrupt(interruptPin));
    time_taken = millis() - timer;
    rpm = (rev * 60000) / time_taken;
    Serial.println(rpm);
    if (rpm >= 400) {
      digitalWrite(switchpin, HIGH);
    }
    else {
      digitalWrite(switchpin, LOW);
    }
    // enable interrupts
    attachInterrupt(digitalPinToInterrupt(interruptPin), revcounter, RISING);
    timer = millis();
    rev = 0;
  }
  else if (flag == 1){
    //sleep 50ms
    delay(50);
    flag = 0;
  }
}

void revcounter() {
  if (flag == 0){
    rev = rev + 1;
    flag = 1;
  }


}