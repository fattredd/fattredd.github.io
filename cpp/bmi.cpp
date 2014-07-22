#include <iostream>
#include <string>

using namespace std;

//////////////////////
//                  //
// Made by fattredd //
//    July 2014     //
//                  //
//////////////////////
// Reference:
//   www.cdc.gov/growthcharts/2000growthchart-us.pdf
//      page 158
//

float calcBMI(int weight,int height) {
	float n = (float)weight*703.0; //numerator
	float d = (float)height*height; //demoninator
	return n/d;
}

float le(float x){return 0.030*(x*x)-0.4524*x+15.33;}//lowerLim
float me(float x){return 0.033*(x*x)-0.136*x+17.6485;}//mediumLim
float ue(float x){return 0.0343*(x*x)-0.0075*x+18.5629;}//upperLim
float ae(int x){return 18.254-1.101*x+0.132*(x*x)-0.00319*(x*x*x);}//avg.

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

int main() {
	int weight;
	int height;
	int age;
	cout<<endl<<endl;
	cout<<"##################"<<endl;
	cout<<"# BMI Calculator #"<<endl;
	cout<<"##################"<<endl;
	cout<<"Enter weight (lbs): ";
	cin>>weight;
	cout<<"Enter height (in): ";
	cin>>height;
	cout<<"Enter age (yrs): ";
	cin>>age;
	float bmi=calcBMI(weight,height);
	cout<<"\n\nYour BMI is "<<bmi;
	cout<<"\nFor your age, you are "<<bmiAverage(bmi,age);
	cout<<"\n\nA normal BMI for your age is ";
	if (age<20){
		cout<<ae(age);
	}else{
		cout<<"18-25";
	}
	cout<<endl<<endl;
	return 0;
}
