#include <iostream>
#include <time.h>
#include <stdlib.h>
#include <limits.h>
#include <stdio.h>

using namespace std;

struct Node{
    string data;
    Node *prev;
    Node *next;
};

class Rstack{
private:
    int sz;
    Node * top;
public:
    Rstack()
    {
        sz = 0;
        top = NULL;
    }
    void push(string s)
    {


        Node *p = new Node;
        p -> data = s;
        if(sz == 0)
        {
            top = p;
            top -> prev = NULL;
            top -> next = NULL;
        }
        else
            {
                if(sz == 1)
                {
                    p -> next = top;
                    p -> prev = top;
                    top -> next = p;
                    top -> prev = p;
                }
                else
                    {
                        p -> prev = top -> prev;
                        p -> next = top;
                        top -> prev -> next = p;
                        top -> prev = p;
                    }

            }

        sz++;
    }
    int getsz()
    {
        return sz;
    }
    string f(int cnt)
    {
        Node *f;
        f = top;
        for(int i = 0; i < cnt - 1; i++)
        {
            f = f -> next;
        }
        return f -> data;
    }
    string pop()
    {
        sz--;
        string f = top -> data;
        Node *t = top -> prev;
        delete top;
        top = t;
        return f;
    }

};

int main()
{
    Rstack q;
    string com, s;
    getline(cin, com);
    int cnt = 0, k = 0;
    for(int i = 0; i < com.size(); i++)
    {
        if(com[i] == ' ') cnt++;
    }
    cnt++;
    while(cin >> s)
    {
        q.push(s);
    }

    cnt = (cnt - 1) % q.getsz() + 1;
    s = q.f(cnt);
    cout << s << endl;

    return 0;
}
