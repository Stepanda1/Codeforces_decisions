import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    pts = [None] * n

    INF = 10**18
    # Инициализируем экстремумы
    x_min = INF; cnt_xmin = 0; x_2min = INF; idx_xmin = -1
    x_max = -INF; cnt_xmax = 0; x_2max = -INF; idx_xmax = -1
    y_min = INF; cnt_ymin = 0; y_2min = INF; idx_ymin = -1
    y_max = -INF; cnt_ymax = 0; y_2max = -INF; idx_ymax = -1

    for i in range(n):
        x, y = map(int, input().split())
        pts[i] = (x, y)

        # x_min / x_2min
        if x < x_min:
            x_2min, x_min = x_min, x
            cnt_xmin, idx_xmin = 1, i
        elif x == x_min:
            cnt_xmin += 1
        elif x < x_2min:
            x_2min = x

        # x_max / x_2max
        if x > x_max:
            x_2max, x_max = x_max, x
            cnt_xmax, idx_xmax = 1, i
        elif x == x_max:
            cnt_xmax += 1
        elif x > x_2max:
            x_2max = x

        # y_min / y_2min
        if y < y_min:
            y_2min, y_min = y_min, y
            cnt_ymin, idx_ymin = 1, i
        elif y == y_min:
            cnt_ymin += 1
        elif y < y_2min:
            y_2min = y

        # y_max / y_2max
        if y > y_max:
            y_2max, y_max = y_max, y
            cnt_ymax, idx_ymax = 1, i
        elif y == y_max:
            cnt_ymax += 1
        elif y > y_2max:
            y_2max = y

    # Стоимость без переноса
    base = (x_max - x_min + 1) * (y_max - y_min + 1)
    answer = base

    # Собираем кандидатов (единственные экстремумы)
    candidates = set()
    if cnt_xmin == 1: candidates.add(idx_xmin)
    if cnt_xmax == 1: candidates.add(idx_xmax)
    if cnt_ymin == 1: candidates.add(idx_ymin)
    if cnt_ymax == 1: candidates.add(idx_ymax)

    # Пробуем «перенести» каждого кандидата
    for i in candidates:
        px, py = pts[i]

        # новые экстремумы без i-го
        nx_min = x_2min if (px == x_min and cnt_xmin == 1) else x_min
        nx_max = x_2max if (px == x_max and cnt_xmax == 1) else x_max
        ny_min = y_2min if (py == y_min and cnt_ymin == 1) else y_min
        ny_max = y_2max if (py == y_max and cnt_ymax == 1) else y_max

        w = nx_max - nx_min + 1
        h = ny_max - ny_min + 1

        # Расширяем при необходимости
        if w * h >= n:
            area_i = w * h
        else:
            W = max(w, (n + h - 1) // h)
            H = max(h, (n + w - 1) // w)
            area_i = min(W * h, w * H)

        answer = min(answer, area_i)

    print(answer)