
## 다익스트라
- 하나의 정점에서 출발시, 다른 모든 정점까지의 최단경로를 구함

### 코드
- [https://www.acmicpc.net/problem/1753](https://www.acmicpc.net/problem/1753)
```python
import sys
input = sys.stdin.readline

# 서로다른 두 정점 사이에, 여러 간선 존재 가능
import heapq

inf = 1000000000

n, e = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1)]
heap = []
ans = [inf for i in range(n+1)]

for i in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((w, v)) # 가중치와 정점

def dijkstra(n):
    
    ans[start]=0
    # heapq.heappush(heap,[0, start]) 보다 1/4 빠르다! 
    heapq.heappush(heap,(0, start))

    while(heap):
        nowWeight, now = heapq.heappop(heap)

        # if ans[now] < nowWeight: # 이해해보자
        #     continue

        for e in graph[now]:
            line = e[0]
            nextNode = e[1]

            nextWeight = nowWeight + line

            if ans[nextNode] > nextWeight:
                ans[nextNode] = nextWeight

                heapq.heappush(heap, (nextWeight, nextNode))


dijkstra(start)
ans.remove(inf)
for e in ans:
    if e==inf:
        print("INF")
    else:
        print(e)
```

## 플로이드 와샬
- 모든 정점에서 다른모든 정점까지의 최단 경로
- 3중 반복문(k, i, j) : graph[i][j]를 구하는데, k점을 거치는 것 고려

- [https://www.acmicpc.net/problem/11404](https://www.acmicpc.net/problem/11404)

### 코드
```python
#입력
n = int(input())
m = int(input())
bus_cost = [[100001 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    bus_cost[start][end] = min(cost, bus_cost[start][end])

#플로이드-워셜 알고리즘
for k in range(1, n+1): #경로 for문이 가장 상위 단계여야 누락되지 않는다
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j: #자기 자신으로 오는 경우는 없다고 했으므로
                bus_cost[i][j] = 0 
            else: #경로 거치는 것 or 직접 가는 것 or 이전 경로들
                bus_cost[i][j] = min(bus_cost[i][j],
                                     bus_cost[i][k] + bus_cost[k][j])


#출력
for row in bus_cost[1:]:
    for col in row[1:]:
        if col == 100001:
            print(0, end = " ")
        else:
            print(col, end = " ")
    print()
```