#include <iostream>
#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <limits.h>

using namespace std;
void init(int *a, int n);
void write(int *a, int n);

int comp(const void *, const void *);
void qsortmy(int *a, int n, int b);
void qsort(void *buf, size_t num, size_t size, int (*compare) (const void *, const void *));

int main()
{
    int n; cin >> n;
    int *a = new int[n];
    qsort(a, n, sizeof(int), comp);
    init(a, n);
    //write(a, n);
    clock_t start, finish;
    double dt;
    start = clock();

    // --------------------------------------------------------------------
    int i1 = rand() % n;

    int i2 = rand() % n;
    int i3 = rand() % n;

    int b = 0;
    if(((a[i1] > a[i2]) && (a[i1] < a[i3])) || ((a[i1] < a[i2]) && (a[i1] > a[i3])))  b = a[i1];
    if(((a[i3] > a[i2]) && (a[i3] < a[i1])) || ((a[i3] > a[i1]) && (a[i2] > a[i3])))  b = a[i3];
    else  b = a[i2];

    // --------------------------------------------------------------------

    qsortmy(a,  n, b);
    finish = clock();
    dt = (double)(finish - start) / CLOCKS_PER_SEC;
    printf( "timemerge = %.6f seconds\n", dt);

    write(a, n);
    delete [] a;
    return 0;
}

void write(int *a, int n) {
	for(int i = 0; i < n; i++)
		cout << a[i] << " ";
	cout << endl;
	cout << endl;
}

void init(int *a, int n)
{
	srand(time(NULL));
	for(int i = 0; i < n; i++)
		a[i] = rand() % 100000;
}

void qsortmy(int *a, int n, int b)
{

    int x = b;
   // cout << x << endl;
    int i = -1;
//    int x = a[n-1];
    for(int j = 0; j < n - 1; j++)
            if(a[j] <= x)
            {
                swap(a[j], a[i + 1]);
                i++;
            }
        swap(a[n - 1], a[i + 1]); // a[i + 1] = x
    //==============================
    int len1 = i + 1;
    int len2 = n - 1 - i - 1;
    if(len1 > 1) qsortmy(a, len1, b);
    if(len2 > 1) qsortmy(a + i + 2, len2, b);

}
int check(int *a, int n)
{
    for(int i = 1; i < n; i++)
    {
        if(a[i] < a[i - 1]) return 0;
    }
    return 1;
}

int comp(const void *i, const void *j)
{
  return *(int *)i - *(int *)j;
}



