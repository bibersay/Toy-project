import sys
input = sys.stdin.readline

def dfs(start,visit,graph):
    global cnt
    visit[start] =True
    cnt +=1

    for g in graph[start]:
        if visit[g] == False:
            dfs(g,visit,graph)


for _ in range(int(input())):

    V , E = map(int,input().split())

    graph = [[] for _ in range(V + 1)]
    visit = [False] * (V + 1)

    for _ in range(E):
        u, v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)

    cnt =-1
    dfs(1, visit, graph)
    print(cnt)



