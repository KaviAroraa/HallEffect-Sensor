void setup() {
  pinMode(26, INPUT);
  Serial.begin(115200);
}

// Global variables
int revolutions = 0;
unsigned long initial = 0;
unsigned long current = 0;
bool si = false;

void loop() {
  // Read the input pin
  bool sf = digitalRead(26);

  if (sf == 1 && si == 0) {
    initial = millis(); // Record the start time
  }
  
  if (sf == 0 && si == 1) {
    current = millis(); // Record the end time
    revolutions++; // Increment revolution count
  }
  
  si = sf;
  
  if (revolutions > 0) {
    unsigned long elapsed = current - initial;
    
    if (elapsed > 0) { // To avoid division by zero
      float rpm = (float)60000 / elapsed;
      
      Serial.print("Elapsed Time (ms): ");
      Serial.println(elapsed);
      Serial.print("RPM: ");
      Serial.println(rpm);
      
      // Reset variables for next measurement
      revolutions = 0;
      initial = 0;
      current = 0;
    }
  }
  
  // Optional delay to slow down the loop for stability
  delay(10); // Adjust as necessary
}
