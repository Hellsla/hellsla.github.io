// Valoanturi sarjaplotteriin (Ruukkilabra, Ahjo 1, tunti 10)
// Kytkenta: 5V -> valovastus -> A0 -> 10 kohm vastus -> GND
// Avaa Tools -> Serial Plotter ja valitse 9600 baud.
// Light sensor to the serial plotter: 5V -> LDR -> A0 -> 10 kohm -> GND, 9600 baud.

const int SENSOR_PIN = A0;      // jannitteenjaon keskikohta / the divider's middle point

void setup() {
  Serial.begin(9600);           // sama nopeus kuin plotterissa / the same speed as the plotter
}

void loop() {
  int value = analogRead(SENSOR_PIN);   // 0...1023 vastaa 0...5 V / 0...1023 means 0...5 V
  Serial.print("valo:");                // nimi kayralle / the curve's name
  Serial.println(value);
  delay(50);                            // 20 lukemaa sekunnissa / 20 readings a second
}
