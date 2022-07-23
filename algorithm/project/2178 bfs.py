import sys
from collections import deque

# input = sys.stdin.readline

i, j = map(int, input().split())
dp = []
for u in range(i):
    dp.append(list(map(int, input())))
#

# for i in range(len(dp)):
#     print(dp[i])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

heap = [(0, 0)]
q = deque(heap)
while q:
    x, y = q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx < 0 or i <= nx or ny < 0 or j <= ny:
            continue
        if dp[nx][ny] == 0:
            continue

        if dp[nx][ny] == 1:
            dp[nx][ny] = dp[x][y] + 1
            q.append((nx, ny))

print(dp[i-1][j-1])
