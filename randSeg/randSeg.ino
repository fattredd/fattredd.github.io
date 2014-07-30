// rand stream to bin,
// then bin to 7-seg (via hex)
// Made for the ATtiny44
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
byte latch = 0;
byte buffer1;
byte buffer2;
byte cur;

void setup(){
  //7-segment output pins
  pinMode(2,OUTPUT);//a
  pinMode(3,OUTPUT);//b
  pinMode(4,OUTPUT);//c
  pinMode(5,OUTPUT);//d
  pinMode(6,OUTPUT);//e
  pinMode(7,OUTPUT);//f
  pinMode(8,OUTPUT);//g
  //bin input stream
  pinMode(1,INPUT);
  //latch
  pinMode(0,INPUT);
  //selectors
  pinMode(9,INPUT);
  pinMode(10,INPUT);
}

byte getVal(int pin) {
  if (digitalRead(pin)==HIGH){
    return 1;
  } 
  else {
    return 0;
  }
}
void loop(){
  latch = getVal(0);
  if (latch==0){
    for (int i=0;i<4;i++) { //get 4 bits to use for the number
      buffer1 = (buffer1<<1) + getVal(1);
      delayMicroseconds(5);
    }
    for (int i=0;i<4;i++) { //get 4 bits to use for the number
      buffer2 = (buffer2<<1) + getVal(1);
      delayMicroseconds(5);
    }
  }
  //first display
  digitalWrite(9,LOW);
  digitalWrite(10,HIGH);
  for (int i=0;i<8;i++){ //turn byte into 7seg
    cur = bitRead(seg[buffer1],i);
    if (cur==1) {
      digitalWrite(i+2,HIGH);
    } else {
      digitalWrite(i+2,LOW);
    }
  }

  //second display
  digitalWrite(10,LOW);
  digitalWrite(9,HIGH);
  for (int i=0;i<8;i++){ //turn byte into 7seg
    cur = bitRead(seg[buffer2],i);
    if (cur==1) {
      digitalWrite(i+2,HIGH);
    } else {
      digitalWrite(i+2,LOW);
    }
  }

}


