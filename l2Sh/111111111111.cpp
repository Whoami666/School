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
string a1, b1, c1 = "";
int a2 = 0, b2 = 0, c2 = 0;
string a, b, c = "";
getline(cin, S);
int n = S.size();
for(int j = 0; j < 3; j++)
{
for(int i = 0; i < n; i++)
{
while(S[i] != ' ')
{
if(S[i] >= '0' && S[i] <= '9')
{
a1 = a1 + S[i];
a = a + S[i];
}

}



}


}
return 0;
}



