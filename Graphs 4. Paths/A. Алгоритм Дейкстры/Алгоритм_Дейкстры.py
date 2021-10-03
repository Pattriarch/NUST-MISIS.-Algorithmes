from collections import defaultdict
import math

n, s, f = [int(x) for x in input().split()]
numbers = [input().split() for x in range(n)]

dict = defaultdict(list)

for i in range(len(numbers)):
    for j in range(len(numbers)):
        if numbers[i][j] != '0' and numbers[i][j] != '-1':
            dict[i+1].append((j+1, int(numbers[i][j])))


d = {i:math.inf for i in range(1, n+1)}
d[s] = 0
parents = {}
used = {i:False for i in range(1, n+1)}
for i in range(1, n+1):
    v = -1
    for j in range(1, n+1):
        if used[j] == False and (v == -1 or d[j] < d[v]):
            v = j
    if d[v] == math.inf:
        break
    used[v] = True

    for j in range(1, len(dict[v])+1):
        to = dict[v][j-1][0]
        length = dict[v][j-1][1]
        if d[v] + length < d[to]:
            d[to] = d[v] + length
            try:
                parents[to] = v
            except:
                pass
if d[f] < math.inf:
    print(d[f])
else:
    print(-1)