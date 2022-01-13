## 그래프

- 정점과 간선으로 이루어진 자료구조. 양방향, 단방향, 가중치 유무.

### 구현

- 인접행렬

- 인접리스트 : 인접행렬보다 공간, 시간적 이득.

vector < pair<int, 가중치> > arr[4];



## DFS

- 깊이 우선 탐색 : 끝까지 갔다가 돌아오는 탐색법.
- 현재 정점에서 갈 수 있는 방문하지 않았던 정점으로 이동.
- 재귀나 스택으로 구현. 재귀가 좀더 쉬운 것 같다.

### 재귀

{
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
}
}



### 스택

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

## BFS

- 넓이 우선 탐색. 매 턴마다 모든 경우에서 한칸씩 전진한다. 최단경로를 찾을 때 유용하다.
