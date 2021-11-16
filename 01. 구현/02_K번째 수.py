import sys
# 입력
T = int(input())
for _ in range(T):
    N, s, e, k = map(int, sys.stdin.readline().split())
    # s - e번째까지 슬라이싱 -> 오름차순
    nums = sorted(list(map(int, sys.stdin.readline().split()))[s-1:e])    
    
    #출력
    print(f'#{_+1} {nums[k-1]}')