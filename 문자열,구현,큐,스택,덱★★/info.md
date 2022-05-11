## 비트연산

-   숫자를 2진수로 연산하는 방법.

    // int는 4byte = 32bit

    int a = 3;
    a = a << 1; // 모든 비트 왼쪽으로: 제곱연산!
    cout << a << endl; // 6

    cout << (~a) << endl; // not

    cout << (a | 1) << endl; // or

    cout << (a & 1) << endl; // and

    cout << (a ^ 1) << endl; // xor

## deque

-   front와 back 둘다에서 pop과 push가 가능한 자료구조.

-   vector.erase(vector.begin()) 보다 deque.pop_front() 가 더 빠르다.
