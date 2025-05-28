import sys
import math

def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        s = input().strip()
        y = int(s)
        k = math.isqrt(y)
        if k ** 2 == y:
            print(0,k)
        else:
            print(-1)
            
if __name__ == '__main__':
    main()