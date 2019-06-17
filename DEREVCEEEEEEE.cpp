#include <iostream>
#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <limits.h>
using namespace std;


struct Node{
    int data;
    Node *left;
    Node *right;
    };
void write(Node *T);
void insTree(Node * &T, int x);


int main()
{
    Node *root = NULL;
    int x;
    cin >> x;
    while(x != 0)
    {
        insTree(root, x);
        cin >> x;
    }
    write(root);

    return 0;
}

void insTree(Node * &T, int x)
{
    if(T == NULL)
    {
        T = new Node;
        T -> data = x;
        T -> left = T -> right = NULL;
    }
    else
    {
        if(x >= T -> data) insTree(T -> right, x);
        if(x < T -> data) insTree(T -> left, x);
    }
}

void write(Node *T)
{
    int cnt = 1;
    int k;
  if(T != NULL)
  {
      write(T -> left);
      if(T -> data != k)
      {
        cout << T -> data << ' ';
        k = T -> data;
      }
      else
      {
        cnt++;
      }

      cout  << cnt << endl;
      cnt = 1;
      //write(T -> right);
  }
}


