nodes = int(input())
links = int(input())
INF = float('inf')
n = nodes + 1
arr = [[INF for i2 in range(n)] for j2 in range(n)]
for ii in range(n):
    arr[ii][ii] = 0
for i3 in range(links):
    a, b, c = map(int, input().split())
    arr[a][b] = min(c, arr[a][b])
for k in range(n):
    for i in range(n):
        if i != k:
            for j in range(n):
                if j != i and j != k:
                    arr[i][j] = min(arr[i][k]+arr[k][j], arr[i][j])
for x in range(1, n):
    for y in range(1, n):
        if arr[x][y] >= INF:
            print(0, end=" ")
        else:
            print(arr[x][y], end=" ")
    print()
