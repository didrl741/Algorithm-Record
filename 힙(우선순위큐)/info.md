
## 주요개념

- priority_queue 란 ? vector와 같은 container로써, 모든 원소 중에서 우선순위가 가장 높은 요소가 top을 유지한다.
- 내부적으로 Heap 자료구조를 사용해서 구현했다. (Heap은 완전이진트리로 만들었다.)
- push(), pop(), top(), empty(), size() 등의 기본적인 메소드가 있다.


## 사용법

    #include <iostream>
    #include <queue>
    using namespace std;

    struct cmp
    {
        bool operator() (int n1, int n2)
        {
            return n1 < n2;
        }
    };

    int main()
    {
        // 우선순위 큐의 세 가지 선언방법.

        priority_queue < int > pq;                  // 가장 큰 값이 top.
        
        priority_queue < int, vector<int> > pq2;

        priority_queue < int, vector<int>, greater<int> > pq3;  // greater, less 두개가 있다.
        
        priority_queue <int, vector<int>, cmp > pq4;
        // 자료형, 컨테이너, 비교클래스(비교함수와는 다르다). 직접 구체적인 비교를 할 수 있다.

        pq4.push(3);
        pq4.push(4);
        pq4.push(1);
        pq4.push(2);
        pq4.push(5);

        while (!pq4.empty())
        {
            cout << pq4.top() << ' ';
            pq4.pop();
        }                               // 5 4 3 2 1
    }