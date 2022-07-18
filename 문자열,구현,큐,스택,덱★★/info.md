# python

## list를 큐, 스택처럼 사용 (느리다)
list는 무작위 접근(random access)에 최적화 된 자료구조이기 때문에 pop(0) 또는 insert(0, x)이 느리다. ( 시간복잡도 = O(n) )
```python
list1 = [1,2,3,4,5]

# 뒤 제거
list1.pop()

print(list1)

# 앞 제거
list1.pop(0)

print(list1)

# 뒤에 삽입
list1.append(0)

print(list1)

# 앞에 삽입
list1.insert(0, 10)

print(list1)

```

## deque (빠르다. 이걸 쓰자.)

덱의 popleft()와 appendleft()는 모두 O(1) 이기 때문에 list의 pop(0)과 insert(0,x) 대비 큰 이점.   
하지만 덱은 내부적으로 연결리스트 구조이기 때문에, random access의 시간복잡도가 O(n) 이다.

### 사용법 

```python
from collections import deque

mydeque = deque([1,2,3])

# 뒤에 추가
mydeque.append(4)       # 1, 2, 3, 4

# 앞에 추가
mydeque.appendleft(0)       # 0, 1, 2, 3, 4

# 뒤에 제거
mydeque.pop()       # 0, 1, 2, 3

# 앞에 제거
mydeque.popleft()       # 1, 2, 3




d1 = deque('abc')

d1.extend('def')        #   오른쪽에 합치기     'a', 'b', 'c', 'd', 'e', 'f'

d1.extendleft('xyz')    # 왼쪽에 합치기.    'z', 'y', 'x', 'a', 'b', 'c', 'd', 'e', 'f'

d1.insert(1, 'k')       # 인덱스에 삽입     'z', 'k', 'y', 'x', 'a', 'b', 'c', 'd', 'e', 'f

d1.remove('k')      # 값 지우기.    'z', 'y', 'x', 'a', 'b', 'c', 'd', 'e', 'f'

d1.reverse()        # 좌우 반전     'f', 'e', 'd', 'c', 'b', 'a', 'x', 'y', 'z'

d1.rotate(3)        # 오른쪽으로 밀고 왼쪽에 붙이기. 'x', 'y', 'z', 'f', 'e', 'd', 'c', 'b', 'a

d1.rotate(-3)       # 왼쪽으로 밀기.       'f', 'e', 'd', 'c', 'b', 'a', 'x', 'y', 'z

print(len(d1))      # 크기

```

## Queue (덱보다 느리다)
모듈이 멀티쓰레드 환경을 지원하기 때문에 덱보다 느리다.
Queue의 성능은 deque와 마찬가지로 데이터 추가/삭제는 O(1), 데이터 접근은 O(N)의 시간 복잡도를 가진다.

```python
from queue import Queue

myque = Queue()

myque.put(1)
myque.put(2)
myque.put(3)

print(myque.get())      # 1
print(myque.get())      # 2
```

# C++

## 비트연산

-   숫자를 2진수로 연산하는 방법.

    // int는 4byte = 32bit

    int a = 3;
    a = a << 1; // 모든 비트 왼쪽으로: 제곱연산!
    cout << a << endl; // 6

    cout << (~a) << endl; // not

    cout << (a | 1) << endl; // or

    cout << (a & 1) << endl; // and

    cout << (a ^ 1) << endl; // xor

## deque

-   front와 back 둘다에서 pop과 push가 가능한 자료구조.

-   vector.erase(vector.begin()) 보다 deque.pop_front() 가 더 빠르다.
