import sys
import heapq

def can_reach(a, k):
    """
    Return True if by splitting elements of array `a` we can increase its length from len(a) to k,
    where splitting means replacing an even x by two copies of x//2.
    """
    need = k - len(a)
    if need < 0:
        return False

    # max-heap of elements (store negatives)
    heap = [-x for x in a]
    heapq.heapify(heap)

    # Try to perform exactly `need` splits
    for _ in range(need):
        # Extract the largest element we can split
        while heap and (-heap[0]) % 2 == 1:
            # top is odd, can't split—pull it aside
            # but we need to keep it for later
            # so we just skip it and reinsert after
            x = -heapq.heappop(heap)
            heapq.heappush(heap, -x)
            # we've tried all odds at top → if top is odd, everything is odd
            # so no more splits possible
            return False

        # Now top must be even
        x = -heapq.heappop(heap)
        half = x // 2
        # split into two halves
        heapq.heappush(heap, -half)
        heapq.heappush(heap, -half)

    # If we succeeded in making `need` splits, we have length k
    return True

def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        print("YES" if can_reach(a, k) else "NO")

if __name__ == "__main__":
    main()
