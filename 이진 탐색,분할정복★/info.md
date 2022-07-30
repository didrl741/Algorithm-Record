
# 주요 개념

-   값이 정렬되어 있을 때 빠르게 탐색 가능.
-   절반씩 탐색하므로 빅 오는 log N
-   DP와 다른점 : DP는 중복이 존재.

# python

## 이진탐색의 두 버전

```python
# 재귀 버전 
def binary(arr, l, r, target):

    if l <= r:
        mid = (l + r) // 2
        
        if arr[mid] == target:
            return True
        elif target > arr[mid]:
            return binary(arr, mid+1, r, target)
        else:
            return binary(arr, l, mid-1, target)
    return False

# 일반 버전 : 조금 더 빠르다.
def binary2(arr, l, r, target):

    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return True
        elif target < arr[mid]:
            r = mid-1
        else:
            l = mid + 1
    return False
```

## 이진탐색 라이브러리

```python
import bisect

list1 = [1,2,3,4,4,5]

print(bisect.bisect_left(list1, 4))     # 3
print(bisect.bisect_right(list1, 4 ))     # 5

print(bisect.bisect_right(list1, 4 ) - bisect.bisect_left(list1, 4) )   # 2 (갯수샐때 유용)
```

# C++

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

    cout << upper_boune(~) - lower_bound(~) : 그 요소의 갯수 찾기.

    cout << binary_search(v.begin(), v.end(), 69);		// 있는지 없는지. (algorighm 헤더)
