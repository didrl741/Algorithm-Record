## 주요개념

-   단순히 라이브러리를 쓰면 되는 것도 있고, 각 정렬을 구현할 줄 알아야 함.
-   비교값이 여러개일 때 -> struct, compare함수 이용하면 편하다.

### 선택정렬

-   처음부터 끝까지 훑으며 가장 작은 원소를 선택해서 바꾸며 올라가는 방식.

### 삽입정렬

-   정렬된 배열에 1개씩 삽입하며 정렬하는 방식.

### 퀵 정렬

-   피벗을 하나 정한다(맨 앞). 그 후, 피벗을 기준으로 왼쪽은 작게, 오른쪽은 크게 만든다.
-   왼쪽과 오른쪽을 피벗정렬한다.

## STL

-   unique(v.begin(), v.end())  
    헤더: algorithm  
    연속으로 중복 되는 원소를 제거한다.  
    연속으로 중복된 값만 제거하기 때문에 반드시 정렬을 하고 해야 한다.  
    중복된 값이 사라져 남게 된 공간은 원본값을 유지한다. 따라서 이 공간을 제거해줘야 진정한 중복 제거 벡터가 된다. 이것은 erase()를 이용한다.

        vector<int> v = { 1,2,2,3,4,4,5,6 };

        unique(v.begin(), v.end());

        for (int i = 0; i < v.size(); i++)
        {
            cout << v[i] << ' ';
        }
        cout << endl;

        vector<int> v2 = { 1,2,2,3,4,4,5,6 };

        // unique는 중복된 첫 원소의 주소를 반환.
        v2.erase(unique(v2.begin(), v2.end()), v2.end());

        for (int i = 0; i < v2.size(); i++)
        {
            cout << v2[i] << ' ';
        }

-   lower_bound(v2.begin(), v2.end(), k)

k값이 v2에서 몇 번째에 위치하는지 주소값을 반환.  
auto it = lower_bound(v2.begin(), v2.end(), k);  
cout << it - v2.begin() 하면 idx가 출력

-   stable_sort : sort와 사용법이 같다. (헤더 : algorithm)

퀵정렬로 구현된 sort 함수는 비교값이 동일할 때 순서가 바뀔 위험이 있다.
하지만 stable_sort는 병합정렬로 구현되어 있기 때문에 같은값이면 순서가 바뀌지 않는다.

-   set (set 헤더)

노드 기반 컨테이너이며, 균형 이진트리로 구현되어있다.  
중복이 허용되지 않는다!!  
원소가 insert에 의해 삽입이 되면, 원소는 자동으로 정렬된다. (디폴트: 오름차순)

-   multiset (set 헤더)

set container와 달리 key가 중복 가능한 set을 구현할 수 있다.  
트리 자료구조로서, 원소를 넣으면 "자동으로 오름차순 정렬" 이 된다!  
insert: 원소 삽입.  
erase: 인자로 값을 넣으면 그 값을 가진 인자 모두 삭제. 주소값을 넣으면 그 주소의 원소만 삭제.

    multiset<int> ms;

    ms.insert(3);
    ms.insert(9);
    ms.insert(6);
    ms.insert(12);
    ms.insert(2);

    cout << *ms.begin() << endl;		//2

    auto it = ms.end();
    it--;
    cout << *it << endl;				// 12

    ms.erase(it);				// 마지막 요소(제일 큰 값) 제거

    it = ms.end();
    it--;
    cout << *it << endl;				// 9


    ms.erase(ms.begin());		// 첫 요소 제거(제일 작은 값)

    cout << *ms.begin() << endl;

    if(ms.find(12)==ms.end()) cout << "없음";       // 못 찾을 시, end() 반환!
