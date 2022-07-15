import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

V, E = list(map(int, input().split()))
start = int(input())

dp = [INF] * (V + 1)
graph = [[] for _ in range(V + 1)]
heap = []

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))


def dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        wei, now = heapq.heappop(heap)

        if dp[now] < wei:
            continue

        for w, next in graph[now]:
            next_wei = w + wei
            if next_wei < dp[next]:
                dp[next] = next_wei
                heapq.heappush(heap, (next_wei, next))


dijkstra(start)
for i in range(1, V + 1):
    print("INF" if dp[i] == INF else dp[i])
