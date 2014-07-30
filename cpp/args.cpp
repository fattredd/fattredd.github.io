#include <iostream>

//////////////////////
//                  //
// Made by fattredd //
//    July 2014     //
//                  //
//////////////////////

int main(int argc,char** args){
	for (int i=0;i<argc;i++){
		std::cout<<i<<" - "<<args[i]<<std::endl;
	}
	//master();
	return 0;
}
