#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <limits.h>
using namespace std;


struct Node{
    string data;
    Node *next;
    Node *prev;
    };


class Stack{
private:

    Node *top;
    int sizen;
public:
    Stack()
    {
        sizen = 0;
        top = NULL;
    }

    int getsize()
    {
        return sizen;
    }
    void Add_element(string x);
    string naming(int sizen);
    string pop();

};




int main()
{
  int sizen = 0;
  Stack poll;
  string schita, print;
  getline(cin, schita);
    for(int i = 0; i < schita.size(); i++)
    {
        if(schita[i] == ' ') sizen++;
    }
    sizen++;


    while(cin >> print)
    {
        poll.Add_element(print);
    }


    print = poll.naming(sizen);


    cout << print << endl;

    return 0;
  }

void Stack::Add_element(string x)
{
    sizen++;
    Node *temp = new Node;   //create a temporary directive
    temp -> prev = top;   //get the top from the previous statement
    temp -> data = x;   //put the element we need to the temp
    top = temp;  //put this directive to the top
}


string Stack::pop()
{
    string f = top -> data;  //create the new variable which shows the thing we needed to delete
    Node *temp = top -> prev; //create a directive which directs to the previous top statement
    delete top; //delete the top statement because we actually need to do this stuff
    top = temp; //now we have a new top
    sizen--;
    return f;
}
string Stack::naming(int sizen)
{
    Node *name;  //create
    name = top;  //put top there
    for(int i = 0; i < sizen - 1; i++)
    {
        name = name -> next;     //move till we get the name we need
    }
    return name -> data;   //return it to print
}
