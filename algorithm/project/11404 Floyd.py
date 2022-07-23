import sys

input = sys.stdin.readline
INF = sys.maxsize

V = int(input())
E = int(input())

dp = [[INF] * (V+1) for _ in range(V+1)]

for _ in range(1,E+1):
    u, v, w = map(int, input().split())
    if dp[u][v] > w:
        dp[u][v] = w


def Floyd():

    for k in range(1,V+1):
        for i in range(1,V+1):
            for j in range(1, V+1):
                if i is not j and dp[i][j] > dp[i][k] + dp[k][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
    return dp

dp = Floyd()

for i in dp[1:]:
    for j in i[1:]:
        if j == INF:
            print(0,end=' ')
        else:
            print(j,end=' ')
    print()