## 문자열 유용한 내장 함수

-   substr(startIdx, len) : string의 일부분을 복사하는 함수.

    string str = "abcde";
    string str2 = str.substr(1, 2);
    // str2 = "bc"

-   stoi(str) : 숫자로 이루어진 string을 int로 바꿔주는 함수.

    string str = "10";
    int n = stoi(str);
    // n=10

-   to_string(num) : 수 num을 string으로 변환.

    int n = 10;

    string str = to_string(n);
    // str = "10"

    double n = 10.01;

    string str = to_string(n);
    // str = "10.010000"

-   숫자가 몇자리 수인지, 또 그 수가 몇인지 : string을 이용하면 편리하다.
    하지만 시간이 약간 더 느리다.
