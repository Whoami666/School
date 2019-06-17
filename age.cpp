#include <iostream>

using namespace std;
struct DATA{
int year, mon, day;};
void age(DATA birth, DATA Today);
int main()
{
    DATA birth, Today ;

    Today.year = 2018;
    Today.mon = 10;
    Today.day = 15;
    cout << "print your date of birth" << endl;
    cin >> birth.year >> birth.mon >> birth.day;
    age(birth, Today);


    DATA * pbirth, *pToday ;
    pbirth = new DATA;
    pToday = new DATA;

    pToday->year = 2018;
    pToday->mon = 10;
    pToday->day = 15;
    cout << "print your date of birth the second time" << endl;
    cin >> pbirth->year >> pbirth->mon >> pbirth->day;
    age(*pbirth, *pToday);

    delete pbirth;
    delete pToday;
    return 0;
}

void age(DATA birth, DATA Today)
{
  int t;
  t = Today.year - birth.year - 1;
  if((Today.mon == birth.mon) && (Today.day > birth.day)) t++;
  else
  {
    if(Today.mon > birth.mon) t++;
  }

  cout << t << " years";
}












