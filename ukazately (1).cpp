#include <iostream>
#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <limits.h>
using namespace std;


struct Node{
    int data;
    Node *next;
    Node *prev;
    };

void Add_element(Node* &pbeg, Node* &pend, int x );
void write(Node *p);



int main()
{
    int n, x;
    Node *pbeg = NULL;
    Node *pend = NULL;
    cin >> n;
    cin >> x;
   // Add_element(pbeg, pend, x);
    for(int i = 0; i < n; i++)
    {
        Add_element(pbeg, pend, x);

    }
    write(pbeg);
}

void Add_element(Node* &pbeg, Node* &pend, int x )
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
        cin >> T ->data;
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



