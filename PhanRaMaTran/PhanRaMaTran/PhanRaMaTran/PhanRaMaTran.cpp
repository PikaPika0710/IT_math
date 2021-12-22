// PhanRaMaTran.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include "Matrix.h"
#include "Polynomial.h"
#include <vector>

using namespace std;
int main()
{
	//Matrix<double> p(4, 4);
	//p.at(0, 0) = 2;
	//p.at(0, 1) = 1;
	//p.at(0, 2) = 4;
	//p.at(0, 3) = 4;

	//p.at(1, 0) = 1;
	//p.at(1, 1) = 2 ;
	//p.at(1, 2) = 5;
	//p.at(1, 3) = 4;

	//p.at(2, 0) = 8;
	//p.at(2, 1) = 7;
	//p.at(2, 2) = 6;
	//p.at(2, 3) = 3;

	//p.at(3, 0) = 26;
	//p.at(3, 1) = 7;
	//p.at(3, 2) = 5;
	//p.at(3, 3) = 2 ;


	Matrix<double> p(2, 2);
	p.at(0, 0) = 2;
	p.at(1, 1) = 2;
	p.at(0, 1) = 1;
	p.at(1, 0) = 1;
	Matrix<double> a,b;
	p.Decomposition(a,b);
	cout << a << endl << b;

}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
