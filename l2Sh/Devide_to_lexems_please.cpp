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
getline(cin, S);
int flag = 0;
int n = S.size();
for(int i = 0; i < n; i++)
{
if(S[i] >= '0' && S[i] <= '9')
{
cout << S[i];
while(S[i + 1] >= '0' && S[i + 1] <= '9')
 {
    cout << S[i+1];
    i++;
 }
cout << endl;
}

else if(S[i] != ' ') cout << S[i] << endl;
}
return 0;
}



