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

while True:
    seq = list(map(int, input().split()))
    if seq[0] == 0:
        exit()
    L = []
    dfs(1, L,seq)
    print()
