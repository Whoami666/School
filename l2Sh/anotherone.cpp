
#include <stdlib.h>
#include <iostream>
#include <stack>
#include <string.h>

using namespace std;

int sizen(string R);
int symbolic(char x);


int main()
{
stack <char> T;
string S, R = "";
getline(cin, S);
int n = S.size();
for(int i = 0; i < n; i++)
{
if(S[i] >= '0' && S[i] <= '9') R = R + S[i];
else if(sizen(R) == 1) R = R + ' ';

if(symbolic(S[i]) == 2)
{
while(!T.empty() && (symbolic(T.top()) == 2) || (symbolic(T.top()) == 3))
{
if(sizen(R) == 1) R = R + ' ';
R = R + T.top();
T.pop();
}
T.push(S[i]);
if(sizen(R) == 1) R = R + ' ';
}

if (S[i] == '(') T.push(S[i]);

if(symbolic(S[i]) == 3)
{
if(!T.empty() && (symbolic(T.top()) == 3))
{
if(sizen(R) == 1) R = R + ' ';
R = R + T.top();
T.pop();
}
T.push(S[i]);
if(sizen(R) == 1) R = R + ' ';
}
if(S[i] == ')')
{
    while(1)
    {
        char x = T.top();
        T.pop();
        if(x == '(') break;
        if(R.size() != 0 && R[R.size() - 1] != ' ') R = R + ' ' + x;
        else R = R + x;
    }
}

}
while(!T.empty())
{

if(sizen(R) == 1) R = R + ' ';
R = R + T.top();
T.pop();
}
cout << R;
return 0;
}

int symbolic(char x)
{
    if((x == '+') || (x == '-' )) return 2;
    if((x == '*') || (x == '/')) return 3;
}

int sizen(string R)
{
    if(R[R.size() - 1] != ' ' && R.size() != 0) return 1;
    else return -1;
}
