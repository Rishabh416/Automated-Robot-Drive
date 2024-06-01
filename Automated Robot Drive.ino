int right1 = 5;
int right2 = 4;
int rightS = 10;

int left1 = 2;
int left2 = 3;
int leftS = 9;

void motorR(bool direction, int speed) {
    float calcSpeed = map(speed, 0, 100, 0, 255);
    digitalWrite(right1, direction);
    digitalWrite(right2, !direction);
    analogWrite(rightS, calcSpeed);

}

void motorL(bool direction, int speed) {
    float calcSpeed = map(speed, 0, 100, 0, 255);
    digitalWrite(left1, direction);
    digitalWrite(left2, !direction);
    analogWrite(leftS, calcSpeed);

}

void setup() {
    Serial.begin(9600);
    pinMode(right1, OUTPUT);
    pinMode(right2, OUTPUT);
    pinMode(rightS, OUTPUT);
    pinMode(left1, OUTPUT);
    pinMode(left2, OUTPUT);
    pinMode(leftS, OUTPUT);
    Serial.println("hello world");
    Serial.begin(9600);

}

void loop() {
    if (Serial.available()) {
        String receivedData = Serial.readStringUntil('\n');
        Serial.println(receivedData); // rm cl 100
        String motor = receivedData.substring(0, 2);
        String direction = receivedData.substring(3, 5);
        int speed = receivedData.substring(6).toInt();
    }
    
}