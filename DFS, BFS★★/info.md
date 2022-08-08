# 그래프

-   정점과 간선으로 이루어진 자료구조. 양방향, 단방향, 가중치 유무.

- 구현:
	- 인접행렬
	-   인접리스트 : 인접행렬보다 공간, 시간적 이득.


# DFS

-   깊이 우선 탐색 : 끝까지 갔다가 돌아오는 탐색법.
-   현재 정점에서 갈 수 있는 방문하지 않았던 정점으로 이동.
-   재귀나 스택으로 구현. 재귀가 좀더 쉬운 것 같다.
-   백트래킹을 이용한 전수조사(N-Queen)방식에도 이용된다.  
    즉, 아니다싶으면 return하여 이전에서 다시 조사하는 방식.

## 재귀

```python
def DFS(n):
    visited[n] = 1

    global ans
    ans+=1

    for e in graph[n]:
        if visited[e] == 0:
            DFS(e)

```


# BFS

-   넓이 우선 탐색. 매 턴마다 모든 경우에서 한칸씩 전진한다. 최단경로를 찾을 때 유용하다.
-   재귀로 구현이 불가능하다. 재귀는 스택과 시스템적으로 구조가 같아서 한번 들어가면
-   들어간 곳에서 끝까지 파고들어가거나 return하기 전까진 나올 수 없기 때문이다.
-   즉, BFS의 특징인 '턴제' 를 구현할 수 없다.

## 큐
```python
def BFS(n):

    deq = deque()

    visited = [0 for i in range(101)]
    visited[n] = 1

    global ans
    
    deq.append(n)

    while(len(deq) != 0):
        tmp = deq[0]
        ans+=1
        deq.popleft()

        for e in graph[tmp]:
            if visited[e]==0:
                deq.append(e)
                visited[e]=1        # 주의!!!
```

<br>
<br>


<br>
<br>


# **C++**

- `vector < pair<int, 가중치> > arr[4];`


# DFS

## 재귀

    void DFS2(int vertex)
    {
    	visited[vertex] = true;
    	ans++;

    	for (int i = 0; i < arr[vertex].size(); i++)
    	{
    		if (visited[arr[vertex][i]] == false)
    		{
    			DFS(arr[vertex][i]);
    		}
    	}

    	visited[vertex] = false;		// 경로마다 따로 체크해야될 사항이 있는 경우, return할 때 false 해주자!!
    }

-   DFS(int vertex, int cnt)를 해서 DFS(newVertex, cnt+1) 할 경우, 그 점의 depth가 cnt가 된다.
-   BFS에서도 마찬가지므로 cnt는 원점에서 그 지점까지의 거리가 된다.

<br>
<br>


## 스택

    void DFS3(int vertex)
    {
    	visited[vertex] = true;
    	st.push(vertex);
    	ans++;

    	while (!st.empty())
    	{
    		// 주의 : 스택은 push하면 top이 바뀐다!
    		int now_top = st.top();
    		st.pop();			// pop 위치 주의!!

    		for (int i = 0; i < arr[now_top].size(); i++)
    		{
    			if (visited[arr[now_top][i]] == false)
    			{
    				visited[arr[now_top][i]] = true;
    				ans++;
    				st.push(arr[now_top][i]);
    			}
    		}
    	}
    }

<br>
<br>


# BFS

## 큐

    void BFS()
    {
    	visited[n] = true;
    	q.push({ n, 0 });			// 큐에는 true 해놓고 넣는다.

    	while (!q.empty())
    	{
    		if (q.front().nowPosition == m)
    		{
    			ans = q.front().cnt;
    			return;
    		}

    		int nowTop = q.front().nowPosition;
    		int nowCnt = q.front().cnt;

    		q.pop();

    		if (nowTop * 2 <= 100000 && !visited[nowTop * 2])
    		{
    			visited[nowTop * 2] = true;
    			q.push({ nowTop * 2, nowCnt + 1 });
    		}

    		if (nowTop + 1 <= 100000 && !visited[nowTop + 1])
    		{
    			visited[nowTop + 1] = true;
    			q.push({ nowTop + 1, nowCnt + 1 });
    		}

    		if (nowTop - 1 >= 0 && !visited[nowTop - 1])
    		{
    			visited[nowTop - 1] = true;
    			q.push({ nowTop - 1, nowCnt + 1 });
    		}
    	}
    }