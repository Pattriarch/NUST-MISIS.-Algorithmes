from collections import defaultdict
import math

n, m = [int(x) for x in input().split()]
s, e = [int(x) for x in input().split()]
numbers = [input().split() for x in range(m)]

dict = defaultdict(list)
for j in range(m):
    for i in range(1, n+1):
        if i == int(numbers[j][0]):
            dict[i].append((int(numbers[j][1]), int(numbers[j][2])/100))
            dict[int(numbers[j][1])].append((i, int(numbers[j][2])/100))


parents = {}
used = {i:False for i in range(1, n+1)}
d = {i:math.inf for i in range(1, n+1)}
d[s] = 0
for i in range(1, n+1):
    v = -1
    for j in range(1, n+1):
        if used[j] == False and (v == -1 or d[j] < d[v]):
            v = j

    for j in dict[v]:
        to = j[0]
        ver = j[1]
        if d[v] == math.inf:
            d[v] = 0
        if d[v] + ver - d[v]*ver < d[to]:
            d[to] = d[v] + ver - d[v]*ver

    used[v] = True

if d[e] != 0:
    print(d[e])
else:
    print(0)
