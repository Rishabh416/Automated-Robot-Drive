int right1 = 5;
int right2 = 4;
int rightS = 10;

int left1 = 2;
int left2 = 3;
int leftS = 9;

void motor(bool direction, int speed) {
    float calcSpeed = map(speed, 0, 100, 0, 255);
    digitalWrite(right1, direction);
    digitalWrite(right2, !direction);
    analogWrite(rightS, calcSpeed);

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

}

void loop() {
    motor(true,50);
    
}