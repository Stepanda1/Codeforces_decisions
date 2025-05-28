import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    s = input().strip()
    cnt0 = s.count('0')
    cnt1 = n - cnt0
    P = n // 2
    z = P - k
    if 0 <= z <= cnt0 and z <= cnt1 and (cnt0 - z) % 2 == 0:
        print("YES")
    else:
        print("NO")