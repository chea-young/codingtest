## python 자주 쓰이는 모듈 정리

### import heapq
- `heapq.heappush(list, element)`
- `heapq.heappop(list)`
- `heapq.heapify(list)`: 기존의 리스트를 힙으로 변환

### from collections import deque
```
deq = deque()

# Add element to the start
deq.appendleft(element)

# Add element to the end
deq.append(element)

# Pop element from the start
deq.popleft()

# Pop element from the end
deq.pop()
```

### import itertools
- `itertools.permutations(list, 갯수)`
- `itertools.combinations(list, 갯수)`