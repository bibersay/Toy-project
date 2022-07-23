import sys
from collections import deque

sys.setrecursionlimit(10 ** 9)
# input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]


def bfs(graph, x, y):
    q = deque([(x,y)])
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    cnt = 1
    graph[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or nx < 0 or ny >= n or ny < 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1
    return cnt


count = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            count.append(bfs(graph, i, j))

count.sort()
print(len(count))
for i in range(len(count)):
    print(count[i])
