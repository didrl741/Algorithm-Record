> [ https://www.acmicpc.net/problem/9019 ]( https://www.acmicpc.net/problem/9019 )   

# 해결 전략

</br>

## 1.  BFS
- 브루트포스 + BFS 느낌이다.
- 입력받은 수로부터 타겟 수까지 shortcut을 찾기 너무 힘들어보이기 때문에, 가지를 DSLR 4개씩 쳐가면서 하나씩 일일이 확인해야 한다.

## 2. L구하기

- 방법1: int를 str으로 변환 후 연산을 거쳐서 다시 int 반환
    - 속도: 11156ms

```python
def L(num):
    strNum = str(num)
    
    len1 = 4 - len(strNum)
    strForAdd = ""

    for i in range(len1):
        strForAdd +='0'

    strNum = strForAdd + strNum
    
    r = strNum[1:] + strNum[0]

    return int(r)
```

- 방법2: 수학적 연산
    - 속도: 7240ms

```python
def L2(num):

    if num<1000:
        return num*10

    tmp = num*10
    tmp =  tmp%10000 + tmp//10000
    return tmp
```

- 방법3: 수학적 연산2
    - 속도: 6572ms (**가장 빠르다!**)

```python
def L3(num):
    return (10*num+(num//1000))%10000
```

## 3. 함수로 구현vs코드 그냥 치기 

- 가시성을 위해 함수로 구현하는 방법과 그냥 코드로 치는 방법 둘 다 써봤다.
- 전자가 더 느릴 줄 알았는데 후자가 너 느렸다!
- 함수 구현 -> 가시성, 속도 둘다 UP

## 4. Pypy3
- pypy3로 해야 정답이다. 다른사람들 코드도 마찬가지.

</br>

# 코드

```python
import sys
from collections import deque

def D(num):
    return (num*2)%10000

def S(num):
    if num==0:
        return 9999
    else:
        return num-1

def L(num):
    strNum = str(num)
    
    len1 = 4 - len(strNum)
    strForAdd = ""

    for i in range(len1):
        strForAdd +='0'

    strNum = strForAdd + strNum
    
    r = strNum[1:] + strNum[0]

    return int(r)

def L2(num):

    if num<1000:
        return num*10

    tmp = num*10
    tmp =  tmp%10000 + tmp//10000
    return tmp

def L3(num):
    return (10*num+(num//1000))%10000

def R(num):
    strNum = str(num)
    
    len1 = 4 - len(strNum)
    strForAdd = ""

    for i in range(len1):
        strForAdd +='0'

    strNum = strForAdd + strNum
    
    r =  strNum[3] + strNum[:3]

    return int(r)

def R2(num):

    tmp = num%10
    r = num//10 + tmp*1000
    return r

def R3(num):
    return (num//10+(num%10)*1000)%10000

def BFS(inNum, rNum):
    deq = deque()

    visited = [ 0 for i in range(10000) ]

    deq.append([inNum, ""])

    visited[inNum] = 1

    while(len(deq)!=0):
        tmp = deq.popleft()
        tmpNum = tmp[0]
        tmpStr = tmp[1]

        if tmpNum==rNum:
            return tmpStr
            
        dResult = D(tmpNum)
        sResult = S(tmpNum)
        lResult = L3(tmpNum)
        rResult = R3(tmpNum)

        if visited[dResult]==0:
            deq.append([dResult, tmpStr + "D"])
            visited[dResult]=1

        if visited[sResult]==0:
            deq.append([sResult, tmpStr + "S"])
            visited[sResult]=1

        if visited[lResult]==0:
            deq.append([lResult, tmpStr + "L"])
            visited[lResult]=1

        if visited[rResult]==0:
            deq.append([rResult, tmpStr + "R"])
            visited[rResult]=1
        
tk = int(sys.stdin.readline())

for i in range(tk):
    inNum, rNum = map(int, sys.stdin.readline().split())
    print(BFS(inNum, rNum))

```