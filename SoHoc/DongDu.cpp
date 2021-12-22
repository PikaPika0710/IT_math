#include<iostream>
#include<cmath>
using namespace std;
int modPrimePow(long a, long b, int p)
{
    long ret = 1;
    a %= p;
    b %= p - 1;
    while (b > 0) //vòng lặp phân tích b thành cơ số 2
    {
        if (b % 2 > 0)  //ở vị trí có số 1 thì nhân với a^(2^i) tương ứng. Tất cả các phép nhân đều có phép mod p theo sau.
            ret = ret * a % p;
        a = a * a % p;  //tính tiếp a^(2^(i+1)), a^1 -> a^2 -> a^4 -> a^8 -> a^16 v.v...
        b /= 2;
    }
    return (int) ret;
}

int main()
{
     long long a = 1234567899;
     long long b = 5461521916;
     int  m = 1000007;
    cout << modPrimePow(a, b, m) << endl; //257419741
}