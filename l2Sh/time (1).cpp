#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;
    struct time{
        int h, m, sec;
         };
void TIME(time A1, time A2);
int main()
{
    time A1, A2;
    cout << "print the first time" << endl;
    cin >> A1.h >> A1.m >> A1.sec;
    cout << "print the second time" << endl;
    cin >> A2.h >> A2.m >> A2.sec;
    TIME(A1, A2);
    cout << endl;

//-----------------------------------------------------------------------------

    time * pA1, *pA2;
    pA1 = new time;
    pA2 = new time;
    cout << "print the first time" << endl;
    cin >> pA1->h >> pA1->m >> pA1->sec;
    cout << "print the second time" << endl;
    cin >> pA2->h >> pA2->m >> pA2->sec;

    TIME(*pA1, *pA2);

    delete pA1;
    delete pA2;
    return 0;
}
void TIME(time A1, time A2)
{
  /*  if(A1.h > A2.h) cout << A1.h - A2.h << " hours" << " ";
    else cout << A2.h - A1.h << " hours" << " ";
    if(A1.m > A2.m) cout << A1.m - A2.m << " minutes" << " ";
    else cout << A2.m - A1.m << " minutes" << " ";
    if(A1.sec > A2.sec) cout << A1.sec - A2.sec << " sec" << "  or  ";
    else cout << A2.sec - A1.sec << " sec" << "  or  ";
*/
    int A11, A22;
    A11 = A1.h*3600 + A1.m*60 + A1.sec;
    A22 = A2.h*3600 + A2.m*60 + A2.sec;


    cout << abs(A22 - A11) << " sec";
}
