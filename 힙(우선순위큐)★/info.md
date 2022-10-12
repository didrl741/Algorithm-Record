
## 주요 개념

- 일반적인 큐와 달리, 자료가 제거될 때 정해진 순서에 따라 자료를 제거하는 자료구조.
- 내부적으로 Heap 자료구조를 사용해서 구현했다. (Heap은 완전이진트리로 만들었다.)
- 삽입 `O(logN)` 삭제 `O(logN)` 의 복잡도를 가진다.
- 디폴트 최대사이즈는 무한대이지만, 최대 크기를 지정할 수 있다. 꽉 찼는지 체크하는 full 함수도 있다.
- PriorityQueue 를 사용하는 방법과 heapq를 사용하는 방법 중, heapq가 약간 더 빠르다.
- 내림차순을 구현할 별도의 방법은 업다. -> -를 붙여서 put 하자.

## 사용법

- heapq 사용

```python
import heapq

pq = []

heapq.heappush(pq, 1)   # pq는 그냥 list인데 append와 다른 점:
heapq.heappush(pq, 3)   # pq[0]이 가장 작게 유지시켜준다.
heapq.heappush(pq, 2)

heapq.heappop(pq) # 1
heapq.heappop(pq) # 2
heapq.heappop(pq) # 3

print(pq[0])    # pop 하지 않고 가장 작은 값 출력


# 리스트를 원소로 둘 수도 있다. 앞 값 먼저 비교.
pq = []

heapq.heappush(pq, [1,-1] )
heapq.heappush(pq, [1,1] )
heapq.heappush(pq, [2,-2] )
heapq.heappush(pq, [2,2] )
```

- 기본 (작은 수가 우선)
```python
from queue import PriorityQueue

pq = PriorityQueue()

pq.put(1)
pq.put(5)
pq.put(4)

print(pq.get())     # 1.  pop과 같은 기능.
print(pq.get())     # 4
print(pq.get())     # 5

print(pq.qsize())     # 0
```
- 우선순위 직접 조작
```python
pq = PriorityQueue()

pq.put( (3, 'hi') )
pq.put( (1, 'hello') )
pq.put( (2, 'kim') )

for _ in range(3):
    print(pq.get())

# (1, 'hello')
# (2, 'kim')
# (3, 'hi')
```

# C++

## 주요개념

- priority_queue 란 ? vector와 같은 container로써, 모든 원소 중에서 우선순위가 가장 높은 요소가 top을 유지한다.
- 내부적으로 Heap 자료구조를 사용해서 구현했다. (Heap은 완전이진트리로 만들었다.)
- push(), pop(), top(), empty(), size() 등의 기본적인 메소드가 있다.


## 사용법

    #include <iostream>
    #include <queue>
    using namespace std;

    struct cmp
    {
        bool operator() (int n1, int n2)
        {
            return n1 < n2;
        }
    };

    int main()
    {
        // 우선순위 큐의 세 가지 선언방법.

        priority_queue < int > pq;                  // 가장 큰 값이 top.
        
        priority_queue < int, vector<int> > pq2;

        priority_queue < int, vector<int>, greater<int> > pq3;  // greater, less 두개가 있다.
        
        priority_queue <int, vector<int>, cmp > pq4;
        // 자료형, 컨테이너, 비교클래스(비교함수와는 다르다). 직접 구체적인 비교를 할 수 있다.

        pq4.push(3);
        pq4.push(4);
        pq4.push(1);
        pq4.push(2);
        pq4.push(5);

        while (!pq4.empty())
        {
            cout << pq4.top() << ' ';
            pq4.pop();
        }                               // 5 4 3 2 1
    }