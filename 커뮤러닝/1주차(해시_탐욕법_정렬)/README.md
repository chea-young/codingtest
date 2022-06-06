## 1주차(해시_탐욕법_정렬)

### :evergreen_tree: Step 2-1. 지문 이해 및 풀이 계획 세우기 "완주하지 못한 선수" - 해시
- 10만명의 데이터일 때 n, nlogn 이면 좋을 것 같다
- 선수의 이름이 몇 번 등장했는지
-  해시
```
def solution(participant, completion):
    d = {}
    for x in participant:
        d[x] = x.get(x, 0) + 1
    for x in completion:
        d[x] -= 1
    
    dnf = [k for k, v in d.items() if v > 0]

    return dnf[0]
```
- 정렬 O(NlogN)
```
def solution(participant, completion):
    paricipant.sort()
    completion.sort()
    for i in rnage(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]
```

#### 자료구조의 선택
- 대신 번호가 주어졌다면 -> 선형 배열 
    - 이름을 일 때 못하는 이유는 영어가 24자라 숫자는 10개인데

#### 해시
- key, 해시 테이블이 존재 -> 인덱스를 대신해서 key로 찾아간다
    - 사람들이 key, 이것을 저장해서 매핑되는 곳이 해시 테이블
- key 에서 hash function을 통해서 해시 테이블에 value가 저장된다.

#### 딕션너리
- 검색: O(1) 시간안에 원소에 접근이 가능
- `d[x] = d.get(x, 0) +1` : x라는 값이 존재하면 x의 값을 아니면 0을 반환해서 1을 더함

</br>

### :evergreen_tree: Step 2-3. 지문 이해 및 풀이 계획 세우기 "가장 큰 수" - 정렬 
- 복잡도 O(n^2) -> 너무 길어진다.
1. 빈 문자열로 수를 초기화한다.
2. 가장 크게 만들 수 이쓴 수를 고른다.
3. 그 수를 현재 수에 이어 붙인다.
4. 이 과정을 반복한다.
- 복잡도 O(nlogn)
1. 빈 문자열로 수를 초기화
2. 수의 모록을 크게 만드는 것 우선으로 정렬한다.
    - 크게 만드는 기준
        - 해당를 반복 시켰을 때 큰 수
3. 그 수를 이어 붙인다.
```
def solution(numbers):
    numbers = [str(x) for x in numbers] #O(n)
    numbers.sort(key=lambda x : (x * 4)[:4], reverse=True) # O(nlogn)
    
    if numbers[0] == '0': # 원소가 0으로만 이루어져 있는 케이스가 있을 수 있기 때문에
        answer = '0' #O(1)
    else:
        answer = ''.join(numbers) # O(n)
    return answer

```