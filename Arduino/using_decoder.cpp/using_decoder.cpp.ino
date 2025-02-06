void setup() {
  // put your setup code here, to run once:
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
}

void incrementalDisplay(int num){
  int a = num & 8;
  int b = num & 4;
  int c = num & 2;
  int d = num & 1;

  digitalWrite(2, ((!a)&&(!d))|| ((!b)&&(!c)&&(!d)));
  digitalWrite(3, ((!a)&&(d)&&(!c))|| ((!a)&&(c)&&(!d)));
  digitalWrite(4, ((!a)&&(b)&&(!c))||((!a)&&(b)&&(!d)||(!a)&&(!b)&&c&&d));
  digitalWrite(5, (a)&&(!b)&&(!c)&&(!d) || (!a)&&(b)&&(c)&&(d));
  
}
void display(int num){
  int a[4];
  for (int i = 0; i < 4; i++){
    a[i] = num & (1 << i);
  }
  for(int i = 3; i >= 0; i--){
    digitalWrite(5-i, a[3-i]);
  }
}
void loop() {
  // put your main code here, to run repeatedly:
  /*
  for(int i = 0; i < 10; i++){
    display(i);
    delay(1000);
  }
  */
  incrementalDisplay(5);
}
