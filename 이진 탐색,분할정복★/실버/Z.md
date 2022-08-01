> [ https://www.acmicpc.net/problem/1074 ]( https://www.acmicpc.net/problem/1074 )   

# 해결 전략

</br>

## 1.  분할정복? 다분탐색?

- 브로콜리처럼 계속 반복되는 구조이므로 바로 분할정복을 떠올렸고, 재귀함수를 짰다.
- 처음에는 r, c위치를 고려하지 않고 4 사분면 다 들어가서 갯수를 count했는데 시간초과가 떴다.
- 그래서 r, c위치를 고려하여 4 사분면 중 1개의 사분면으로만 재귀를 호출하여 해결했다.
- 분할정복 보다는 다분탐색이 더 적절하다고 생각한다. (맞는 곳으로만 재귀 호출)

- 하지만 단순 실수로 인해 계속 메모리초과가 나서 while문으로도 작성했다.

## 2. 단순 실수

- 처음에 코드를 아래처럼 짜서 1시간정도 고민했다. (현재위치 x, y고려를 안했다.)
```python
    if r >= size//2:
        tmp+=1
    if c >= size//2:
        tmp+=10
```


</br>

# 코드

## 재귀 사용

```python
import sys
sys.setrecursionlimit(10**6)

n, r, c = map(int, input().split())

global ans
ans =0

def solv(size, y, x):

    global ans
    if size==1 and y==r and x==c:
            return ans

    tmp = 0
    if r >= y+ size//2:             # 현재 사분면에서 r, c가 1,2,3,4 분면중 어디있는지 체크하기 위함
        tmp+=1
    if c >= x + size//2:
        tmp+=10

    if tmp==0:
        return solv(size//2, y,x)

    if tmp==10:
        ans+=size*size // 4
        return solv(size//2, y,x+size//2)

    if tmp==1:
        ans+=size*size // 2
        return solv(size//2, y+size//2,x)

    if tmp==11:
        ans +=size*size // 4 * 3
        return solv(size//2, y+size//2,x+size//2)

print(solv(2**n, 0, 0))
```

## 반복문 사용

```python
n, r, c = map(int, input().split())

ans =0

size = 2**n
x, y = 0, 0

while(True):
    if size==1 and y==r and x==c:
        break

    tmp = 0
    if r >= y + size//2:
        tmp+=1
    if c >= x + size//2:
        tmp+=10

    if tmp==10:
        ans+=size*size // 4
       
        x = x+size//2

    if tmp==1:
        ans+=size*size // 2
        y = y+size//2

    if tmp==11:
        ans +=size*size // 4 * 3
        x = x+size//2
        y = y+size//2

    size = size//2

print(ans)
```