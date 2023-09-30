
## 다중리스트의 주소문제

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

## 전치행렬, 90도회전 행렬
```python
# 1 2 3   7 4 1
# 4 5 6   8 5 2
# 7 8 9   9 6 3
arr = [[1,2,3],[4,5,6],[7,8,9]]

# 전치
arr2 = list(list(e) for e in zip(*arr))

# 전치 -> 90도회전
arr2 = [list(reversed(e)) for e in arr2]

tmpGraph = [[0,0,0],[0,0,0],[0,0,0]]

# 디폴트 90도 회전
for i in range(3):
    for j in range(3):
        tmpGraph[j][3-i-1] = arr[i][j]


for e in tmpGraph:
    print(e)
print('')
```