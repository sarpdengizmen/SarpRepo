#include <LiquidCrystal_I2C.h>
#include <Wire.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);


const byte interruptPin = 2;
bool val;
const byte switchpin = 3;
volatile int rev = 0;
unsigned long timer = 0;
unsigned long time_taken = 0;
long rpm = 0;
bool flag = 0;
const int N = 5; // Number of values to keep for rolling average
unsigned long rev_times[N];
int index = 0;

void setup() {
  pinMode(interruptPin, INPUT);
  pinMode(switchpin, OUTPUT);
  Serial.begin(9600);   
  attachInterrupt(digitalPinToInterrupt(interruptPin), revcounter, RISING);
  timer = millis();
  lcd.init();
  lcd.backlight();
}

void loop() {
  
  if (rev >= 1) {
    // disable interrupts
    detachInterrupt(digitalPinToInterrupt(interruptPin));
    time_taken = micros() - timer;
    Serial.println(time_taken);
    rpm = (60000000) / time_taken;
    timer = micros();
    rev_times[index] = rpm;
    index = (index + 1) % N;
    rpm = average(rev_times, N);
    Serial.println(rpm);
    if (rpm >= 400) {
      digitalWrite(switchpin, HIGH);
    }
    else {
      digitalWrite(switchpin, LOW);
    }
    rev = 0;
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("RPM: ");
    lcd.print(rpm);
    // enable interrupts
    attachInterrupt(digitalPinToInterrupt(interruptPin), revcounter, RISING);
  }
}

// Function to calculate average of an array
unsigned long average(unsigned long* arr, int length) {
  unsigned long sum = 0;
  for (int i = 0; i < length; i++) {
    sum += arr[i];
  }
  return sum / length;
}

void revcounter() {
  // Software debouncing
  static unsigned long last_interrupt_time = 0;
  unsigned long interrupt_time = micros();
  if (interrupt_time - last_interrupt_time > 10000) { // Ignore interrupts closer than 1000 microseconds
    rev++;
  }
  last_interrupt_time = interrupt_time;
}

