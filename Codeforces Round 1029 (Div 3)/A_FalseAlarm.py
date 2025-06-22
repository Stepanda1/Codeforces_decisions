t = int(input())
for _ in range(t):
    n,x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    first = last = -1
    for i in range(len(a)):
        if a[i] == 1:
            first = i
            break
    a.reverse()
    for i in range(len(a)):
        if a[i] == 1:
            last = len(a)-i
            break
    if x < last-first:
        print("NO")
    else:
        print("YES")