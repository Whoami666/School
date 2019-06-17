#include<stdio.h>
#include <iostream>
#include <time.h>
#include <stdlib.h>
#include <stack>
#include <limits.h>
#include <string>
using namespace std;

int main()
{
stack <char> T;
string S, R;
float a1 = 0, b1 = 0, c1 = 0;
int a2 = 0, b2 = 0, c2 = 0;
string a = 0, b = 0, c = 0;
getline(cin, S);
int n = S.size();
for(int j = 0; j < 3; j++)
{
for(int i = 0; i < n; i++)
{
while(S[i] != ' ')
{
    a = a + (S[i]);
}
while(S[i] != ' ')
{
    b = b + (S[i]);
}
while(S[i] != ' ')
{
    c = c + (S[i]);
}
cout << a << ' ' << b << ' ' << c << endl;

}


}
return 0;
}



