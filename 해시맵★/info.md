
# 주요개념

- Key 와 Value의 쌍으로 이루어져있으며, Key를 통해 Value에 빠르게 접근할 수 있다.
- 해시는 정렬이 필요 없으며, 빠른 검색을 원할 때 사용한다.
- 많은 자료를 저장하고, 검색 속도가 빨라야 할 경우 사용.
- 해시맵은 해시 함수를 통해 Key를 특정 값으로 변환시키고 이 값을 Value를 저장할 공간의 인덱스로 사용한다.

</br>

# dictionary

> 값 추가 (key, value)

        d = {}

        d[999] = 10
        d['wow'] = 100
        d[1] = [1,2,3,4,5]
        d[(1,2)] = 99
        d[3] = (1,2,3)

> 값 접근 1

        print(d[999])           # 10
        print(d[ 'wow' ])       # 100
        print(d[ 1 ])               # [1,2,3,4,5]
        print(d[ (1,2) ])          # 99
        print(d[ 3 ])                  # (1,2,3)
        # print(d[999999])  에러

>  값 접근 2: get 

        print(d.get(999))   # 10
        print(d.get(9999999))   # None


>  값 변경

        d[999] = 999
        print(d[999])       # 999

> in - 해당 키가 있는가?

        if 999 in d:
        print('999가 딕셔너리에 있다')

> in - 해당 value가 있는가?

        if 100 in d.values():
        print('value 100이 딕셔너리에 있다')


> keys - 키 나열하기

        # d.keys()의 반환값은 리스트이다!
        print(d.keys())     # [999, 'wow', 1, (1, 2), 3]

        for k in d.keys():
        print(k)

> values - 값 나열하기

        print(d.values()) # [999, 100, [1, 2, 3, 4, 5], 99, (1, 2, 3)]


> items - 키, 값 쌍으로 뽑기

        print(d.items()) # [(999, 999), ('wow', 100), (1, [1, 2, 3, 4, 5]), ((1, 2), 99), (3, (1, 2, 3))]


> del - 키, 값 한 쌍 지우기

        del d['wow']

>  dic의 key로 list는 불가능하지만 튜플은 가능하다. # dic[[0,1]] 에러

        dic = dict()

        dic[(0,1)] = []
        dic[(0,1)].append([3,4,5])
        dic[(0,1)].append([6,7,8])

        dic2 = dict(dic) # 깊은복사

</br>

# 유용한 내장함수
## 1. Counter   (from collections import Counter)

</br>

- 리스트를 인자로 넘기면 요소를 key로, 요소의 갯수를 value로 만든 dict를 반환한다.

```python
from collections import Counter

dict = Counter(['a','a','a','b','b','c'])

# {'a': 3, 'b': 2, 'c': 1}

```


# c++

## 1. unordered_map

- 해시 테이블로 구현되어있기 때문에, 요소를 자동으로 정렬하지 않으며 검색, 삽입, 삭제가 평균적으로 상수 시간( O(1) )에 가능하다.

- 해쉬맵 문제는 이걸로 구현하면 된다.

- 사용법   ( #include <unordered_map> )

        unordered_map<int, string> hm;

        hm.insert({ 3, "apple" });
        hm.insert({ 3, "banana" });
        hm.insert({ 4, "boy" });
        hm.insert({ 5, "orange" });

        cout << hm[3] << endl;      // apple
        cout << hm.at(3) << endl;   // apple. 느림, 안전.
        cout << hm.count(3) << endl;
        cout << hm.size() << endl;  // 3. 서로다른 Key의 수?

        hm.at(4) = "girl";
        hm.erase(5);                // Ket = 5인 원소 삭제.



        // hm.begin() : 첫번째 원소 반복자
        // hm.end() : 마지막 원소 반복자
        // hm.find(key) : 반복자 리턴, 없다면 end 리턴.
        
## 2. map

- Key값 기준으로 sorting 되어있으며 이진탐색트리로 구현되어있기 때문에, unordered_map 보다 찾는데 오래걸린다.

- 사용법 (#include <map>) 나머지는 위와 같다.
