##주요 개념

- 값이 정렬되어 있을 때 빠르게 탐색 가능.
- 절반씩 탐색하므로 빅 오는 log N
- DP와 다른점 : DP는 중복이 존재.


## 이진탐색의 두 버전

![이분탐색](https://user-images.githubusercontent.com/97036481/148726179-4a8d4a9b-1517-40b9-8f8e-41dd8a311c6b.png)
<img src="![이분탐색](https://user-images.githubusercontent.com/97036481/148726179-4a8d4a9b-1517-40b9-8f8e-41dd8a311c6b.png)" width = "500px" height = "600px">??


## 이분탐색 STL

	vector <int> v = { 10,20,30,40,50,60,70 };
	
	vector<int> ::iterator it;

	it = lower_bound(v.begin(), v.end(), 40);		// 40 이상의 값들 중 가장 작은 값
	
	cout << *it << endl;

	it = upper_bound(v.begin(), v.end(), 40);		// 초과.

	cout << *it << endl;

	int x = lower_bound(v.begin(), v.end(), 40) - v.begin() ;

	cout << x << endl;		// 위치

	cout << binary_search(v.begin(), v.end(), 69);		// 있는지 없는지.
    