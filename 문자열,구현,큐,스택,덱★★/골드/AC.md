> [ https://www.acmicpc.net/problem/5430 ]( https://www.acmicpc.net/problem/5430 )   

# 해결 전략

</br>

## 1.  `list[1:-1]`
- 처음에 입력받을 때 특이하게 `[`, `]`를 포함해서 받는다.
- 이 때 list에 대해 `[1:-1]` 하면 처음과 마지막 인자를 날릴 수 있다.

## 2. reverse 고려
- 시간초과의 주범이다.
- 입력함수 최대길이가 100000이기 때문에 R이 최대 100000번 실행될 수 있다.
- 배열의 최대 수 갯수도 100000이기 때문에 reverse()가 O(n) 인것을 고려하면
- 100,000 X 100,000 = 10,000,000,000. 즉 100억이나 된다.
- 따라서 flag를 두었다.

## 3. 출력
- `getList = [123, 345]` ,  `getList2 = ["123","345"]` 라고 하자.
- 아래와 같은 함수로 getList, getList2 둘 다 출력결과에 잘 맞지만 실패. (이유는 모르겠다.)
```python
def printList(list1):
    print('[', end='')
    for e in list1:
        if e!=list1[-1]:
            print(e, end=',')
        else:
            print(e, end='')
    print(']')
```
- 아래 출력법으로 getList2를 넣으면 성공한다. (getList는 오류)
- `print('[' + ",".join(getList2) + ']')`

- 추측: 예를들어서 print(list) 하면 출력결과는 똑같아보이지만 String으로 출력하는것이 아니라 IDE에 따라서 다르게 출력하는게 아닐까..?


</br>

# 코드

## 정답 코드

```python

from collections import deque

n = int(input())

for i in range(n):

    zeroFlag = False
    reverseFlag = False
    
    command = input()
    size = int(input())

    if size==0:
        getList = input()
        getList = deque()
    else:
        getList = input()[1:-1].split(',')
        getList = deque(getList)

    for e in command:
        if e=='R':
            if reverseFlag==False:
                reverseFlag = True
            else:
                reverseFlag = False

        else:
            if len(getList)==0:
                zeroFlag = True
                break
            if reverseFlag == False:
                getList.popleft()
            else:
                getList.pop()

    if zeroFlag == False:
        
        if reverseFlag == True:
            getList.reverse()
        print('[' + ",".join(getList) + ']')
            
    else:
        print("error")
```

## 오류 코드 (이유는 모름)
```python

from collections import deque

n = int(input())

def printList(list1):
    print('[', end='')
    for e in list1:
        if e!=list1[-1]:
            print(e, end=',')
        else:
            print(e, end='')
    print(']')

for i in range(n):

    zeroFlag = False
    reverseFlag = False
    
    command = input()
    size = int(input())

    if size==0:
        getList = input()
        getList = deque()
    else:
        getList = input()[1:-1].split(',')
        getList = list(map(int, getList))
        getList = deque(getList)

    for e in command:
        if e=='R':
            if reverseFlag==False:
                reverseFlag = True
            else:
                reverseFlag = False

        else:
            if len(getList)==0:
                zeroFlag = True
                break
            if reverseFlag == False:
                getList.popleft()
            else:
                getList.pop()

    if zeroFlag == False:
        getList = list(getList)
        if reverseFlag == True:
            getList.reverse()
        
        printList(getList)
            
    else:
        print("error")
```

## c++

```c++
일단 vector로 시도해봤다.
algorithm 헤더의 reverse함수를 이용해봤더니 시간초과가 났다.
R이 나타날 때마다 매번 이 함수를 호출하면 시간초과가 난다.
그래서 R이 나타나면 bool reverseFlag를 이용해서 간접적으로 reverse 해봤다.

하지만 이것 역시도 틀렸다. 여러가지를 생각한 끝에 다음 4가지를 다
고려해야 한다는 것을 알았다.

1. 두자릿수 이상의 숫자 처리
2. string의 숫자들을 컨테이너에 push하기 위해 파싱할때의 소요시간.
3. reverse의 소요시간.
4. vector.erase(vector.begin()) 과 deque의 pop_front()의 소요시간 차이


우선 이 코드는 vector를 이용했고 1, 2, 4 때문에 실패.

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int tk;
int n;
string str;
string str2;
vector<int> v;
bool errorFlag;
bool reverseFlag;

void printVector()
{
	cout << '[';

	if (reverseFlag == true)
	{
		for (int i = v.size()-1; i >= 0; i--)
		{
			if (i == 0) cout << v[i];
			else cout << v[i] << ',';
		}
	}

	else
	{
		for (int i = 0; i < v.size(); i++)
		{
			if (i == v.size() - 1) cout << v[i];
			else cout << v[i] << ',';
		}
	}

	

	cout << ']' << '\n';
}

int main()
{
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	cin >> tk;
	while (tk--)
	{
		cin >> str;
		cin >> n;
		cin >> str2;

		for (int i = 1; i <= 2 * n - 1; i += 2)
		{
			v.push_back(str2[i] - '0');
		}

		int len = str.length();

		for (int i = 0; i < len; i++)
		{
			if (str[i] == 'R')
			{
				//reverse(v.begin(), v.end());
				if(reverseFlag==false) reverseFlag = true;
				else reverseFlag = false;
			}
			else if (str[i] == 'D')
			{
				if (v.empty())
				{
					errorFlag = true;
					break;
				}
				else
				{
					if (reverseFlag == true)
					{
						v.pop_back();
					}
					else
					{
						v.erase(v.begin());
					}
					
				}
			}
		}

		if (errorFlag == true)
		{
			cout << "error" << '\n';
		}
		else
		{
			printVector();
		}

		errorFlag = false;
		reverseFlag = false;
		v.clear();
	}
}


1, 2, 3, 4를 다 고려하여 다음과 같은 코드를 짜서 해결했다.
2번 고려사항에서 3가지 방법을 써봤다.
그 중 방법3을 유의해서 보자. 굉장히 유용해보인다.

#include <iostream>
#include <string>
#include <deque>

using namespace std;

int tk;
int n;

string str;
string str2;

bool errorFlag;
bool reverseFlag;

deque<int> dq;

void printVector()
{
	cout << '[';

	if (reverseFlag == true)
	{
		for (int i = dq.size() - 1; i >= 0; i--)
		{
			if (i == 0) cout << dq[i];
			else cout << dq[i] << ',';
		}
	}

	else
	{
		for (int i = 0; i < dq.size(); i++)
		{
			if (i == dq.size() - 1) cout << dq[i];
			else cout << dq[i] << ',';
		}
	}

	cout << ']' << '\n';
}

int main()
{
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	cin >> tk;
	while (tk--)
	{
		string s;
		cin >> str;
		cin >> n;
		cin >> str2;

		if (n != 0)
		{

			// 방법1: 시간초과, 복잡하다. 내가 처음에 생각.
			/*for (int i = 1; i <= str2.length() - 1; i++)
			{
				if (isdigit(str2[i]))
				{
					if (metDigit == false)
					{
						startDigit = i;
						metDigit = true;
					}

					digitLen++;
				}
				else
				{
					int num = stoi(str2.substr(startDigit, digitLen));
					dq.push_back(num);

					metDigit = false;
				}
			}*/

			// 방법2: 36ms로 가장 빠르다. 조금 더 복잡하다.
			/*int i = 1;

			while (str2[i] != '\0') {
				int x = 0;
				while (str2[i] >= '0' and str2[i] <= '9') {
					x *= 10;
					x += int(str2[i] - '0');
					i++;
				}
				if (x != 0) {
					dq.push_back(x);
				}
				i++;
			}*/


			// 방법 3: 가장 편하다, 48ms
			for (int i = 0; i < str2.length(); i++) {

				if (isdigit(str2[i])) {
					s += str2[i];

				}
				else {
					if (!s.empty()) {
						dq.push_back(stoi(s));
						s = "";
					}
				}
			}
		}


		int len = str.length();

		for (int i = 0; i < len; i++)
		{
			if (str[i] == 'R')
			{
				reverseFlag = !reverseFlag;
			}
			else if (str[i] == 'D')
			{
				if (dq.empty())
				{
					errorFlag = true;
					break;
				}
				else
				{
					if (reverseFlag == true)
					{
						dq.pop_back();
					}
					else
					{
						dq.pop_front();
					}

				}
			}
		}

		if (errorFlag == true)
		{
			cout << "error" << '\n';
		}
		else
		{
			printVector();
		}

		errorFlag = false;
		reverseFlag = false;
		dq.clear();
	}
}
```