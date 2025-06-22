t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    if n == 2:
        # Упростим вручную для n=2
        # a1 = x*1 + y*2
        # a2 = x*2 + y*1
        # Решаем систему
        det = 1*1 - 2*2  # -3
        dx = a[0]*1 - 2*a[1]
        dy = 1*a[1] - 2*a[0]
        if dx % det == 0 and dy % det == 0:
            x = dx // det
            y = dy // det
            print("YES" if x >= 0 and y >= 0 else "NO")
        else:
            print("NO")
    else:
        lhs = 2 * a[0] - a[1]
        if (n + 1) == 0 or lhs % (n + 1) != 0:
            print("NO")
            continue
        y = lhs // (n + 1)
        if y < 0:
            print("NO")
            continue
        x = a[1] - a[0] + y
        if x < 0:
            print("NO")
            continue
        ok = True
        for i in range(n):
            expected = x * (i + 1) + y * (n - i)
            if expected != a[i]:
                ok = False
                break
        print("YES" if ok else "NO")
