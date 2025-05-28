import sys
from collections import deque

def divisors(n):
    """ Return sorted list of all divisors of n. """
    small, large = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            small.append(i)
            if i*i != n:
                large.append(n//i)
        i += 1
    return small + large[::-1]

def solve():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        x, y, k = map(int, input().split())
        # If x == y, no operations needed.
        if x == y:
            print(0)
            continue
        # If x doesn't divide y, impossible
        if y % x != 0:
            print(-1)
            continue

        # Enumerate divisors of y and index them
        dvs = divisors(y)
        D = len(dvs)
        idx = {d: i for i, d in enumerate(dvs)}

        # Build graph on these D nodes
        adj = [[] for _ in range(D)]
        # Multiplication edges: d -> d*q if q <= k
        for i, d in enumerate(dvs):
            for j in range(i+1, D):
                d2 = dvs[j]
                if d2 % d == 0:
                    q = d2 // d
                    if q <= k:
                        adj[i].append(j)
        # Exponentiation edges: d -> d^a if 2 <= a <= k
        for i, d in enumerate(dvs):
            if d == 1:
                continue
            for a in range(2, k+1):
                val = pow(d, a)
                if val > y:
                    break
                if y % val == 0:
                    adj[i].append(idx[val])

        # BFS from x to y
        start = idx[x]
        target = idx[y]
        dist = [-1] * D
        dq = deque([start])
        dist[start] = 0
        while dq:
            u = dq.popleft()
            if u == target:
                break
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    dq.append(v)

        print(dist[target])

if __name__ == "__main__":
    solve()

