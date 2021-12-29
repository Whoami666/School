#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <limits.h>
using namespace std;


struct Node{
    int data;
    Node *next;
    Node *prev;
    };
void Add_element(Node* &pbeg, Node* &pend, int x);
void write(Node *p);

int main()
{
    Node *pbeg = NULL;
    Node *pend = NULL;
    int klass, minclass, number;
    int i = 0;
    string lastname;
    string names, classes;

        while(cin >> klass)
        {
             cin >> lastname;
             classes+ = klass;
             classes+ = " ";
             names+ = lastname;
             names+ = " ";
        }
        minclass = min(classes);
        number = classes.find(minclass);

}
void Add_element(Node* &pbeg, Node* &pend, int x)
{
    if(pbeg == NULL)
    {
        pbeg = new Node;
        pbeg -> data = x;
        pbeg -> next = NULL;
        pbeg -> prev = NULL;
        pend = pbeg;
    }
    else
    {
        Node *T = new Node;
        pend -> next = T;
        T -> prev = pend;
        T -> next = NULL;
        T -> data = x;
        pend = T;
    }
}

void write(Node *p)
{
    Node *t = p;
    while(t != NULL)
    {
        cout << t -> data << " "<<  "->" << " ";
        t = t -> next;
    }
}


