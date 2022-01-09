#include <iostream>
using namespace std;

int main()
{
	int N, K;
	int r = 0;

	cin >> N >> K;

	int arr[10] = { 0, };

	int i;

	for (i = 0; i < N; i++)
	{
		cin >> arr[i];
	}		//i = 9

	while (true)
	{
		if (arr[i] > K)
		{
			i--;
		}
		else
		{
			r += K / arr[i];
			K = K % arr[i];

			if (K == 0) break;

			i--;
		}
	}
	cout << r;
}