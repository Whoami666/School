#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <limits.h>
using namespace std;

int main()
{
 int n;
 int maximum = 0;
 int cnt = 0;
 cin >> n;
 int a[n], b[n];
 int m = n;
 for(int i = 0; i < n; i++)
 {
     cin >> a[i];
 }
 int thestate;
 if(n > 0) thestate = a[0];
 else
 {
   thestate = 0;
 }


for(int i = 0; i < n; i++)
 {
     b[i] = a[i];
 }

 for(int j = 0; j < n; j++)
 {
  for(int i = 0; i < m; i++)
   {
        while(a[j] == b[i])
        {
          if(i == m) b[i] = b[i-1];
          else
          {
            b[i] = b[i-1];

          }
        }
   }

   for(int i = 0; i < m; i++)
   {
       if(b[i] != b[i-1]) cnt++;
   }

   if(cnt > maximum)
   {
     maximum = cnt;
     thestate = a[j];
   }
   cnt = 0;
   m = n;
   for(int i = 0; i < n; i++)
   {
     b[i] = a[i];
   }
 }
 cout << maximum << ' ' << thestate;
 return 0;
}
