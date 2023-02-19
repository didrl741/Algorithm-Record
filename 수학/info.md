
# 순열과 조합

## 순열

- 조합보다 구현이 쉽다.

```python
list1 = [1,2,3,4]

used = [0 for i in range(4)]

def perm(arr,cnt):
    if cnt==2:
        print(arr)
        return
        
    for i in range(4):
        if used[i] == 0:
            used[i]=1
            arr.append(list1[i])
            perm(arr, cnt+1)
            arr.pop()
            used[i]=0
    
perm([],0)
```

## 조합1

- 구현이 쉽지 않다.
- nCr = (n-1)C(r-1) + (n-1)C(r) 을 이용한다.
- 시간이 많이 걸린다.

```python
list1 = [1,2,3,4]

ansArr = []

# list[cnt]를 포함하여  (n-1)C(r-1) 그리고 포함하지 않고 (n-1)C(r) 를 구하는 함수
def combine(arr,cnt):
    print(arr, cnt)

    if cnt==len(list1):
        if len(arr)==2:
            tmp = [i for i in arr]
            ansArr.append(tmp)
        return

    arr.append(list1[cnt])
    combine(arr, cnt+1)
    arr.pop()
    combine(arr, cnt+1)
    
combine([],0)
print(ansArr)
```

## 조합2

- for 반복문을 이용한다. 구현이 쉽다.
- 시간도 더 적게 걸린다. brute force에 가깝다.

```python
list1 = [1,2,3,4]
len = len(list1)

for i in range(len-2):
    for j in range(i+1, len-1):
        print(list1[i], list1[j])
```

## 조합3

- DFS를 이용했다. 구현이 쉽고 빠르다.
- 결과 형식이 약간 다르다.

```python
arr = [0,0,0,0]

def DFS(cnt,idx,target):
    if cnt==target:
        print(arr)
        return
    
    for i in range(idx,4):
        arr[i]=1
        DFS(cnt+1,i+1, target)
        arr[i]=0

DFS(0,0,2)
```

## 조합4

- itertools의 combination 이용
- 삼성에서는 사용 불가능