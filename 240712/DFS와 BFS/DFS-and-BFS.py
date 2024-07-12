import sys
from collections import deque
input = sys.stdin.readline

n, m, num = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[a].sort()
    graph[b].append(a)
    graph[b].sort()

dfs_result = []
v = [False] * (n+1)

def dfs(x, v):
    dfs_result.append(x)
    v[x] = True
    for node in graph[x]:
        if v[node] == False:        
            dfs(node, v)

dfs(num ,v)
print(" ".join(map(str, dfs_result)))


bfs_result = []
v = [False] * (n+1)
queue = deque()
queue.append(num)

while queue:
    x = queue.popleft()
    if v[x] == False:
        v[x] = True
        bfs_result.append(x)
        for i in graph[x]:
            queue.append(i)

print(" ".join(map(str, bfs_result)))