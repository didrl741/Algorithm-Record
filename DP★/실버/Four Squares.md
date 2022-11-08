> [ https://www.acmicpc.net/problem/17626 ]( https://www.acmicpc.net/problem/17626 )   

# 해결 전략

</br>

## 0.  구글링
- 구글링으로 풀었다. 나중에 다시 풀어보자.

## 1.  DP

- 특정 n에서의 값을 구할 때 이전의 값들이 필요하다 -> DP 사용.
- 예를 들어, DP[10] = DP[9] + 나머지(1)처리 = 1 + DP[1]
- 예를 들어, DP[8] = DP[4] + 나머지(4)처리 = 1 + DP[4]


</br>

# 코드

```python
N = int(input())
dp = [0,1]

for i in range(2, N+1):
    min_value = 1e9
    j = 1

    while (j**2) <= i:
        min_value = min(min_value, dp[i - (j**2)])
        # print(i,j, min_value)
        j += 1

    dp.append(min_value + 1)
print(dp[N])
```