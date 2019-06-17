#include <iostream>
#include <stdio.h>

using namespace std;

int a[100][100], visited[100], n, f;

void dfs(int v);

int main()
{
	int m, x, y;
	cin >> n >> m;
	f = 0;
	for (int i = 0; i < n; i++)
	{
		a[i][i] = 0;
	}
	for (int i = 0; i < m; i++)
	{
		cin >> y >> x;
		a[x - 1][y - 1] = 1;
		a[y - 1][x - 1] = 1;
	}
	for (int i = 0; i < n; i++)
	{
		visited[i] = 0;
	}
		for (int i = 0; i < n && f == 0; i++)
	{
		if (visited [i] == 0)
		{
			visited [i] = 1;
			dfs(i);
		}
	}

	if (f == 0)
	cout << "YES";
	else
	cout << "NO";


return 0;
}

void dfs(int v)
{

	for (int j = 0; j < n && f == 0; j++)
	{
		if (a[v][j] != 0)
		{
			if (visited[j] == 0)
			{
				visited [j] = - visited [v];
				dfs(j);
			}
			else if (visited [j] == visited [v])
			{
				f = 1;
			}
		}

	}
}
