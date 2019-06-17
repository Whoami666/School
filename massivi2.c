#include <stdio.h>
#include <limits.h> //неогр. числа(почти)
#include <locale.h> //€зык

int check(int a[], int n);
void print(int a[], int n);
void inc(int a[], int n);
void merge1(int a[], int b[], int c[], int n, int m);
void merge2(int a[], int b[], int c[], int n, int m);
int main()
{
    int a[100 + 1], b[100 + 1], c[200];

    setlocale(LC_ALL,"Rus"); //добавл€ем русский €зык
    int key, n = 100, m = 100;
    int l;
    l = m + n;
    do
    {
        system("cls");                   //то, что вид€т люди
        printf("¬ведите два упор€доченных по неубыванию массива\n");
        printf("===> ");
        inc(a, n);
        inc(b, m);
    }
    while(check(a, n) * check(b, m) == 0);

    do
    {
        printf("¬ыберите алгоритм сли€ни€ массивов:\n");      //то, что вид€т люди
        printf("1 - обычный\n");
        printf("2 - с барьером\n");
        printf("0 - выход\n===> ");
        scanf("%d", &key);
        switch (key)
        {
            case 1: system("cls"); merge1(a, b, c, n, m);
             print(c, l); printf("\n");
             break;
            case 2: system("cls"); merge2(a, b, c, n, m);
             print(c, l); printf("\n");
             break;
            default: system("cls");
        }
    }
    while (key != 0);

    return 0;
}
void vvod(int a[], int n)
{
    int p;
    for(p = 0; p < n; ++p)
    {
        scanf("%d", &a[p]);
    }
}
void print(int a[], int n)
{
    int i;
    for(i = 0; i < n; ++i)
    {
        printf("%d ", a[i]);int i = 0, j = 0, k = 0;
    }
}
int check(int a[], int n)
{
    int i;
    for(i = 0; i < n - 1; ++i)
    {
        if(a[i] > a[i + 1]) return 0;
    }
    return 1;
}
void merge1(int a[], int b[], int c[], int n, int m)
{
    int i = 0, j = 0, l = 0;
    while(i < n && j < m)
    {
        if(a[i] < b[j])
        {
            c[l] = a[i];
            ++i;
            ++l;
        }
        else
        {
            c[l] = b[j];
            ++j;
            ++l;
        }
    }
    while(i < n)
    {
        c[l] = a[i];
        ++l;
        ++i;
    }
    while(j < m)
    {
        c[l] = b[j];
        ++l;
        ++j;
    }

}
void merge2(int a[], int b[], int c[],int n, int m)
{
    int i = 0, j = 0, l = 0;
    a[n] = INT_MAX;
    b[m] = INT_MAX;
    while(l < m + n)
    {
        if(a[i] < b[j])
        {
            c[l] = a[i];
            ++i;
            ++l;
        }
        else
        {
            c[l] = b[j];
            ++j;
            ++l;
        }
    }
}
