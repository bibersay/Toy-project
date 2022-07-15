import sys

sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline


def dfs(start,L,S):

    if 6 <= len(L):
        print(*L)
        return

    for i in range(start, len(S)):
        L.append(S[i])
        dfs(i+1,L,S)
        L.pop()


N, M = list(map(int, input().split()))
