#include<iostream>
#include<cmath>
using namespace std;
bool check(int n)
{
    int sum = 0;
    for (int i = 1; i <= n / 2; i++)
    {
        if (n % i == 0)
            sum += i;
    }
    if (sum == n)
        return true;
    return false;
}
int main()
{
    int n;
    cout << "Nhap n: ";
    cin >> n;
    int i;
    cout << "So hoan hao tu 1 den " << n << " la: ";
    for (i = 1; i <= n; i++)
    {
        if (check(i))
            cout << i << " ";
    }
    return 0;
}