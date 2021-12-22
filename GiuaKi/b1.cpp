#include<iostream>
using namespace std;
int soUoc(int n) {
	int count = 0;
	for (int i = 1 ; i <= n; i++) {
		if(n % i == 0) count++;
	}
	return count;
}

int tongCacUoc(int n) {
	int sum = 0;
	for (int i = 1 ; i <= n; i++) {
		if(n % i == 0) sum+=i;
	}
	return sum;
}
unsigned long long tichCacUoc(int n){
    unsigned long long p = 1;
	for (int i = 1 ; i <= n; i++) {
		if(n % i == 0) p*=i;
	}
	return p;
}
unsigned long long tichCacUoc(int n){
    unsigned long long p = 1;
	for (int i = 1 ; i <= n; i++) {
		if(n % i == 0) p*=i;
	}
	return p;
}
int main(){
    int N = 10000;
    int S = 0;
    int count = 0;
    cout << "So cac uoc so cua N la: " << soUoc(N) << endl;
    cout << "Tong cac uoc so cua N la: " << tongCacUoc(N) << endl;
    cout << "Tich cac uoc so cua N la: " << tichCacUoc(N) << endl;

}
