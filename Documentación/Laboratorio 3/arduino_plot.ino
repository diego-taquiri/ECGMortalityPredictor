/*************************************
 Course: ISB-UPCH
 Date: 29/03/2023
 Autor: Moises Meza

**************************************/

unsigned long lastMsg = 0;
float F=5;                      // 1 hz
double Fs = 10*F;               // 10 hz
double Ts_ms = (1/Fs)*1000;     //  100 ms  

void setup() {
  Serial.begin(9600);
  while (!Serial);
  //Serial.println("R1:,R2:,");
}

void loop() {

  unsigned long now = millis();

  if (now - lastMsg > Ts_ms) {
    
    lastMsg = now;

    //int r1 = random(10);
    //int r2 = random(10);
    int r1 = analogRead(A0);
    //int r2 = analogRead(pin);

    Serial.print("Señal1:");
    Serial.println(r1);
    //Serial.print(",");
    //Serial.print("Señal2:");
    //Serial.println(r2);
  }

}