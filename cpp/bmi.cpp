#include <iostream>
#include <string>

using namespace std;

float calcBMI(int weight,int height) {
	float n = (float)weight*703.0; //numerator
	float d = (float)height*height; //demoninator
	return n/d;
}

float le(float x){return 0.035*(x*x)-0.4524*x+15.33;}
float me(float x){return 0.033*(x*x)-0.136*x+17.6485;}
float ue(float x){return 0.0343*(x*x)-0.0075*x+18.5629;}

string bmiAverage(float bmi,int age) {
	if (age<20) {
		if (bmi<le(bmi)) return "underweight";
		if (bmi>=le(bmi)&&bmi<=me(bmi)) return "normal";
		if (bmi>me(bmi)&&bmi<=ue(bmi)) return "overweight";
		if (bmi>ue(bmi)) return "obese";
		return "one sec";
	} else {
		if (bmi<18.5) return "underweight";
		if (bmi<=18.5&&bmi<=24.9) return "normal";
		if (bmi>=25.0&&bmi<=29.9) return "overweight";
		if (bmi>30.0) return "obese";
	}
}

void master() {
	int weight;
	int height;
	int age;
	cout<<"\n##################\n";
	cout<<"# BMI Calculator #\n";
	cout<<"##################\n";
	cout<<"Enter weight: ";
	cin>>weight;
	cout<<"Enter height: ";
	cin>>height;
	cout<<"Enter age: ";
	cin>>age;
	float bmi=calcBMI(weight,height);
	cout<<"\nYour BMI is "<<bmi;
	cout<<"\nFor your age, you are "<<bmiAverage(bmi,age);
	cout<<endl<<endl;
}

int main(int argc, char* argv[]) {
	master();
	return 0;
}
