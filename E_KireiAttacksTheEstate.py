import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    t = int(input())
    out = []
    for _ in range(t):
        n = int(input())
        a = [0] + list(map(int, input().split()))

        g = [[] for _ in range(n+1)]
        for _ in range(n-1):
            u, v = map(int, input().split())
            g[u].append(v)
            g[v].append(u)

        parent = [0] * (n+1)
        order  = []
        visited = [False] * (n+1)

        # BFS from root=1
        dq = deque([1])
        visited[1] = True
        parent[1] = -1
        while dq:
            u = dq.popleft()
            order.append(u)
            for v in g[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    dq.append(v)

        dp_plus  = [0] * (n+1)
        dp_minus = [0] * (n+1)

        # base at root
        dp_plus[1]  =  a[1]
        dp_minus[1] = -a[1]

        # in BFS order parents before children
        for u in order[1:]:
            p = parent[u]
            # either stop at u, or go to p and continue with flipped sign
            dp_plus[u]  = max(a[u],  a[u] + dp_minus[p])
            dp_minus[u] = max(-a[u], -a[u] + dp_plus[p])

        # collect result for this test
        out.append(" ".join(str(dp_plus[i]) for i in range(1, n+1)))

    # print all at once
    print("\n".join(out))


if __name__ == "__main__":
    solve()
