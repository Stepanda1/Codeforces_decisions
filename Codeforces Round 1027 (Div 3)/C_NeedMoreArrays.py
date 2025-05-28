t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    last = -10**18
    cnt = 0
    for x in a:
        if x - last >= 2:
            cnt += 1
            last = x
    print(cnt)