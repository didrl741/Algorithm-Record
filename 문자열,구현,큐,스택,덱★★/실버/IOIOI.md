> [ https://www.acmicpc.net/problem/5525 ]( https://www.acmicpc.net/problem/5525 )   

# 해결 전략

</br>

## 1.  check 성공시 다음 check는 더 간단하게
- 내가 푼 풀이에서 적용한 방법이다.
- 한번 성공했으면 그 뒤가 OI 이기만 하면 또 성공이기 때문에 이 부분을 구현했다.
- 하지만 인덱스 검사가 피곤했다.

## 2. 파이썬의 for문 주의사항
- for문 내부에서 i에 연산을 해봤자 소용없다!!

```python
for i in range(10):
    print(i)
    i+=5
    print(i)
```
- 위 코드에서 `i+=5` 해봤자 포문의 i에는 영향을 미치지 못한다.
- 이럴때는 `while`을 써야한다.

## 3. 시간복잡도
- 내가 푼 풀이는 다른사람들 코드보다 약 8배가 더 걸렸다.
- 그 이유는 s에서 타겟문자열이 맞는지 검사하는 부분 때문.
- check 필요 없이 s의 처음부터 끝까지 쭉 가면서 연산하는게 훨씬 빠르다. (count 변수 이용)

</br>

# 코드

## 내가 푼 풀이 (2500ms)

- check 성공시, 그 뒤 2글자가 "OI"이면 또 성공
- 체크를 두번하기 때문에 인덱스 검사가 피곤하다.
- s가 클수록 시간이 많이걸릴것이다.

```python
n = int(input())
m = int(input())
s = input()
ans=0

target = "I" + n*"OI"

len = 1+2*n

i=0

while(i < m - len + 1):
    
    if s[i:i+len] == target:
        ans+=1

        while(i+len+2 < m):

            if s[i+len:i+len+2] == "OI":
                ans+=1
                i+=2
            else:
                i += len-1
                break

    i+=1
    
print(ans)
```

## 다른사람들 코드 (300ms)

- count 변수를 이용해서 s의 인덱스 0부터 끝가지 쭉 연산해나가는 방식. 훨씬 빠르다.

```python
N = int(input())
M = int(input())
S = input()
answer, i, count = 0, 0, 0

while i < (M - 1):
    if S[i:i+3] == 'IOI':
        i += 2
        count += 1
        if count == N:
            answer += 1
            count -= 1
    else:
        i += 1
        count = 0

print(answer)
```