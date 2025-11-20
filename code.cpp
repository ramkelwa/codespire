#include <iostream>
using namespace std;

int main()
{
    char s[100];
    cout << "enter string:";
    cin >> s;

    for (int i = 1; s[i] != '\0'; i += 2)
    {
        cout << s[i];
    }
}