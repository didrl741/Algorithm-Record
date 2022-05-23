## 그리디

-   현 상황에서 지금 당장 좋은 것만 고르는 방법.
-   어떤 알고리즘도 생각나지 않을 때 유용.
-   최소 스패닝 트리 (크루스칼, 프림)
-   다익스트라

### 다익스트라

-   어떤 한 노드를 기준으로 그 노드와 나머지 노드와의 최단 경로를 구하는 알고리즘이다.
-   우선순위 큐를 이용하면 빠르다.

-   코드 ( 골드에서 최단경로 문제 참고 )

    struct Atom
    {
        int v;
        int dist;
    };
    
    void dijkstra(int startV)
    {
        priority_queue pq; // startV와의 거리가 가까운것이 top

        pq.push({ startV, 0 });         // 처음 시작점 push

        while (!pq.empty())
        {
            int minDist = pq.top().dist;
            int minIdx = pq.top().v;

            pq.pop();

            for (int k = 0; k < arr[minIdx].size(); k++)
            {
                  if (minIdx를 거쳐서 가는게 더 짧은 노드가 있으면)
                  {
                      ansArr[더 짧아진 노드] = minDist + (minIdx와 더 짧아진 노드 사이의 거리);
                      pq.push({ 더 짧아진 노드 , 갱신된 거리 });
                  }
            }
        }
    }