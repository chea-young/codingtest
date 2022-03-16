# 입력
import sys
p, q = map(int, sys.stdin.readline().split())

number = []
for i in range(p):
    if p%(i+1) == 0:
        number.append(i+1)

# 출력
if len(number) < q:
    print(-1)
else:
    print(number[q-1]) 

# -----------------------------------
# ver 2 
# 입력
import sys
p, q = map(int, sys.stdin.readline().split())

count = 0
for i in range(p):
    if p%(i+1) == 0:
        count += 1
    if count == q:
        print(i+1)
        break
else:
    print(-1)