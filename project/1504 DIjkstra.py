import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

v1, v2 = map(int, input().split())


def Dijk(start):
    dp = [INF] * (V + 1)
    dp[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        weight, node = heapq.heappop(heap)

        if dp[node] < weight:
            continue

        for Next, w in graph[node]:
            Next_weight = dp[node] + w
            if Next_weight < dp[Next]:
                dp[Next] = Next_weight
                heapq.heappush(heap, (Next_weight, Next))
    return dp


one = Dijk(1)
v1_ = Dijk(v1)
v2_ = Dijk(v2)
cnt = min(one[v1] + v1_[v2] + v2_[V], one[v2] + v2_[v1] + v1_[V])

print(cnt if cnt < INF else -1)
