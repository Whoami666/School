#include <stdio.h>
#include <locale.h>
#include <limits.h>
int check(int a[], int n);
void print(int a[], int n);
void vvod(int a[], int n);
void merge1(int a[], int b[], int c[], int n, int m);
void merge2(int a[], int b[], int c[], int n, int m);
int main()
{
    int a[100 + 1], b[100 + 1], c[200];

    setlocale(LC_ALL,"Rus");
    int key, n = 100, m = 100;
    int k;
    k = m + n;
    do
    {
        system("cls");
        printf("Ââåäèòå äâà óïîðÿäî÷åííûõ ïî íåóáûâàíèþ ìàññèâà\n");
        printf("===> ");
        vvod(a, n);
        vvod(b, m);
    }
    while(check(a, n) * check(b, m) == 0);

    do
    {
        printf("Âûáåðèòå àëãîðèòì ñëèÿíèÿ ìàññèâîâ:\n");
        printf("1 - îáû÷íûé\n");
        printf("2 - ñ áàðüåðîì\n");
        printf("0 - âûõîä\n===> ");
        scanf("%d", &key);
        switch (key)
        {
            case 1: system("cls"); merge1(a, b, c, n, m); print(c, k); printf("\n"); break;
            case 2: system("cls"); merge2(a, b, c, n, m); print(c, k); printf("\n"); break;
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
    int i = 0, j = 0, k = 0;
    while(i < n && j < m)
    {
        if(a[i] < b[j])
        {
            c[k] = a[i];
            ++i;
            ++k;
        }
        else
        {
            c[k] = b[j];
            ++j;
            ++k;
        }
    }
    while(i < n)
    {
        c[k] = a[i];
        ++k;
        ++i;
    }
    while(j < m)
    {
        c[k] = b[j];
        ++k;
        ++j;
    }

}
void merge2(int a[], int b[], int c[],int n, int m)
{
    int i = 0, j = 0, k = 0;
    a[n] = INT_MAX;
    b[m] = INT_MAX;
    while(k < m + n)
    {
        if(a[i] < b[j])
        {
            c[k] = a[i];
            ++i;
            ++k;
        }
        else
        {
            c[k] = b[j];
            ++j;
            ++k;
        }
    }
}
