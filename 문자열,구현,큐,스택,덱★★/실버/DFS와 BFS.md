> [ https://www.acmicpc.net/problem/1260 ]( https://www.acmicpc.net/problem/1260 )   

# 해결 전략

</br>

## 특별한 것 없이 기본적인 DFS, BFS 구현하는 문제이다.



</br>

# 코드

```python
from collections import deque

n, m, v = map(int, input().split())

connectList = []
visited = [0 for i in range(1001)]
visited2 = [0 for i in range(1001)]
for i in range(n+1):
    connectList.append([])

for i in range(m):
    a, b = map(int, input().split())
    connectList[a].append(b)
    connectList[b].append(a)

for e in connectList:
    e.sort()

def DFS(v):
    print(v, end=' ')
    visited[v]=1

    for e in connectList[v]:
        if visited[e] == 0:
            DFS(e)



def BFS(v):
    mydeque = deque()
    mydeque.append(v)
    visited2[v]=1

    while(len(mydeque) != 0):
        tmp = mydeque.popleft()
        print(tmp, end=' ')

        for e in connectList[tmp]:
            if visited2[e]==0:
                visited2[e]=1
                mydeque.append(e)

DFS(v)
print()
BFS(v)
```