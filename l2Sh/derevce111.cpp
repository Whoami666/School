#include <iostream>
#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <limits.h>
using namespace std;


struct Node{
    int data;
    Node *left;
    Node *right;
    };
void write(Node *T);
void insTree(Node * &T, int x);
int height(Node *T);
int newhight(Node *T);

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
  //  write(root);
    if(newhight(root) == 5) cout << "NO";
    else cout << "YES";


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
        if(x > T -> data) insTree(T -> right, x);
        if(x < T -> data) insTree(T -> left, x);
    }
}

void write(Node *T)
{
  if(T != NULL)
  {
      write(T -> left);
      cout << T -> data << endl;
      write(T -> right);
  }
}

int height(Node *T)
{
    if(T == NULL) return 0;
    else
    return max( height(T -> right),  height(T -> left)) + 1;
}
int newhight(Node *T)
{
    if((height(T->right) - height(T->left)) > 1) return 5;
    else
    {
      if((height(T->right) - height(T->left)) < -1) return 5;
        else return 6;
    }

}
