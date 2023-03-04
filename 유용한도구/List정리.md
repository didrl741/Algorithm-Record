
# 다중리스트의 주소문제

```python
# 입력값
# 5
# 2 3 2 3 2
# 2 3 2 3 2
# 2 3 2 3 2
# 2 3 2 3 2
# 2 3 2 3 2

n = int(input())

graph = [ [1 for i in range(5)] for j in range(5) ] # 기본 이중 리스트

graph1 = [ list([0,0] for j in range(5)) for i in range(5) ] # 삼중리스트 표현 1
graph1 = [ [ [0,0] for j in range(5) ] for i in range(5) ] # 삼중리스트 표현 2. 이걸 쓰자.
graph2 = [ [[0,0]]*5 for i in range(5) ] # 쓰면 안될 표현. 한 행에 있는 1중리스트들의 주소가 같다!!!

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        graph1[i][j][1] = tmp[j]
        graph2[i][j][1] = tmp[j]
    
graph1[0][0][1]=10
graph2[0][0][1]=10

for e in graph1:
    print(e)

print(' ')

for e in graph2:
    print(e) #결과를 보자.
```
