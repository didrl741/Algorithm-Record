
## 주요개념

- Key 와 Value의 쌍으로 이루어져있으며, Key를 통해 Value에 빠르게 접근할 수 있다.
- 해시는 정렬이 필요 없으며, 빠른 검색을 원할 때 사용한다.
- 많은 자료를 저장하고, 검색 속도가 빨라야 할 경우 사용.
- 해시맵은 해시 함수를 통해 Key를 특정 값으로 변환시키고 이 값을 Value를 저장할 공간의 인덱스로 사용한다.


### unordered_map

- 해시 테이블로 구현되어있기 때문에, 요소를 자동으로 정렬하지 않으며 검색, 삽입, 삭제가 평균적으로 상수 시간에 가능하다.

- 사용법
        unordered_map<int, string> hm;

        hm.insert({ 3, "apple" });
        hm.insert({ 3, "banana" });
        hm.insert({ 4, "boy" });
        hm.insert({ 5, "orange" });

        cout << hm[3] << endl;      // apple
        cout << hm.at(3) << endl;   // apple. 느림, 안전.
        cout << hm.count(3) << endl;
        cout << hm.size() << endl;  // 3. 서로다른 Key의 수?

        hm.at(4) = "girl";
        hm.erase(5);                // Ket = 5인 원소 삭제.



        // hm.begin() : 첫번째 원소 반복자
        // hm.end() : 마지막 원소 반복자
        // hm.find(key) : 반복자 리턴, 없다면 end 리턴.
