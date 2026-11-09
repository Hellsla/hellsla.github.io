// Robotin testiohjelma (Ruukkilabra, Ahjo 1, tunnit 12-13)
// Arduino Uno, kaksi DC-moottoria ja kaksikanavainen moottorinohjain (L298N-tyyppinen: ENA/IN1/IN2 ja ENB/IN3/IN4).
// Testaamaton luonnos: Ahjon robottialustaa ei ole viela valittu. Tarkista pinnit oman moottorinohjaimesi mukaan.
// Moottorit saavat virran omasta paristosta moottorinohjaimen kautta, ei Arduinon 5V-pinnista. GND-pinnit yhteen.
// Nosta robotti ensin pyorat ilmassa telineen paalle ja kokeile vasta sitten lattialla.
// Robot test sketch: Arduino Uno, two DC motors, an L298N-type driver. Untested draft: check the pins for your driver.
// The motors take their power from their own battery through the driver, never from the 5V pin. Join the GNDs.

const int ENA = 5, IN1 = 7, IN2 = 8;    // vasen moottori / left motor (ENA: nopeus PWM / speed)
const int ENB = 6, IN3 = 9, IN4 = 10;   // oikea moottori / right motor

const int SPEED = 160;                  // 0...255; aloita pienella / start low
const int DRIVE_MS = 1000;              // ajoaika / driving time
const int TURN_MS = 400;                // kaannos, saada niin etta kulma on 90 astetta / adjust until the turn is 90 degrees

void motor(int en, int a, int b, int speed) {   // speed -255...255
  digitalWrite(a, speed > 0); digitalWrite(b, speed < 0);
  analogWrite(en, abs(speed));
}

void drive(int left, int right, int ms) {
  motor(ENA, IN1, IN2, left); motor(ENB, IN3, IN4, right);
  delay(ms);
  motor(ENA, IN1, IN2, 0); motor(ENB, IN3, IN4, 0);
  delay(500);                           // tauko / pause
}

void setup() {
  int pins[] = {ENA, IN1, IN2, ENB, IN3, IN4};
  for (int p : pins) pinMode(p, OUTPUT);
  delay(3000);                          // aikaa laskea robotti alas / time to put the robot down
  drive(SPEED, SPEED, DRIVE_MS);        // eteen / forwards
  drive(-SPEED, -SPEED, DRIVE_MS);      // taakse / backwards
  drive(SPEED, -SPEED, TURN_MS);        // kaannos oikealle / turn right
  drive(-SPEED, SPEED, TURN_MS);        // kaannos vasemmalle / turn left
}

void loop() {
  // Tunti 13: ajakaa nelio toistamalla neljasti drive(SPEED, SPEED, DRIVE_MS) ja drive(SPEED, -SPEED, TURN_MS).
  // Lesson 13: drive a square by repeating forwards and a right turn four times.
}

// Tunti 13, anturikokeilu: painike robotin keulaan pinnin 2 ja GND:n valiin. Lisaa setup()-osaan
//   pinMode(2, INPUT_PULLUP);
// ja aja eteenpain vain, kun painike ei ole painettuna (painettuna digitalRead(2) on LOW):
//   if (digitalRead(2) == HIGH) { motor(ENA, IN1, IN2, SPEED); motor(ENB, IN3, IN4, SPEED); }
//   else { motor(ENA, IN1, IN2, 0); motor(ENB, IN3, IN4, 0); }
// Lesson 13, sensor trial: a push button on the robot's front between pin 2 and GND, pinMode(2, INPUT_PULLUP),
// and drive forwards only while digitalRead(2) is HIGH (the button is not pressed); otherwise stop.
