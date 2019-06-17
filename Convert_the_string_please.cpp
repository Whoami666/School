#include<stdio.h>
#include <iostream>
#include <time.h>
#include <stdlib.h>
#include <stack>
#include <limits.h>
#include <string>
using namespace std;

int symbolic(char x);


int main()
{
stack <char> T;
string S, R;
getline(cin, S);
int n = S.size();
for(int i = 0; i < n; i++)
{
  if(S[i] >= '0' && S[i] <= '9') R = R + S[i] + ' ';
  else
  {
      if(T.empty() || S[i] == '(') T.push(S[i]);
      else
      {
          if(S[i] == ')')
          {
            char k = T.top();
            T.pop();
            while(symbolic(k) <= symbolic(T.top()))
            {
             R = R + T.top() + ' ';
             T.pop();
            }

            if(T.top() == '(') T.pop();
          }
          else
          {
            char k = T.top();
            T.pop();
            while(symbolic(S[i]) <= symbolic(T.top()))
            {
             R = R + T.top() + ' ';
             T.pop();
            }
            T.push(S[i]);
          }
      }
}
}
cout << R;
return 0;
}
int symbolic(char x)
{
    if((x == '*') || (x == '/')) return 2;
    else
    {
         if((x == '+') || (x == '-')) return 1;
         else return -1;
    }

}





