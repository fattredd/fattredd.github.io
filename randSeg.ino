// rand stream to bin,
// then bin to 7-seg (via hex)
const byte seg[16] = {
  0b1111110,//0
  0b0110000,
  0b1101101,
  0b1111001,//3
  0b0110011,
  0b1011011,
  0b1011111,//6
  0b1110000,
  0b1111111,
  0b1111011,//9
  0b1110111,
  0b0011111,
  0b1001110,//c
  0b0111101,
  0b1001111,
  0b1000111//f
};
bit latch = 0;
byte buffer;
bit cur;

void setup(){
  //7-segment output pins
  pinMode(3,OUTPUT);//a
  pinMode(4,OUTPUT);//b
  pinMode(5,OUTPUT);//c
  pinMode(6,OUTPUT);//d
  pinMode(7,OUTPUT);//e
  pinMode(8,OUTPUT);//f
  pinMode(9,OUTPUT);//g
  //bin input stream
  pinMode(2,INPUT);
  //latch
  pinMode(10,INPUT);
}
bit getVal(int pin) {
  if (digitalRead(pin)==HIGH){
    return 1;
  } else {
    return 0;
  }
}
void loop(){
  latch = getVal(10);
  for (int i=0;i<4;i++) { //get 4 bits to use for the number
    buffer = (buffer<<1) + getVal(2);
    delayMicroseconds(5);
  }
  Serial.println(buffer,seg[buffer]); //print the buffer
  for (int i=0;i<8;i++){ //turn byte into 7seg
    cur = bitRead(seg[buffer],i);
    if (latch==0) { //don't update if latched
      if (cur==1) {
        digitalWrite(i+3,HIGH);
      } else {
        digitalWrite(i+3,LOW);
      }
    }
  }
}
