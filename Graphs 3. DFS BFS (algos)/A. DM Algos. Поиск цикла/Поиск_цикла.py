from collections import defaultdict
import numpy as np

n = int(input())

a = []
b = []
p = {}

numbers = np.array([input().split() for i in range(int(n))])
used = {i: 0 for i in range(1, n + 1)}

smejn = defaultdict(list)
for i, j in enumerate(numbers):
    for k, l in enumerate(j):
        if l == '1':
            smejn[i + 1].append(k + 1)

cycle = False
def dfs(v):
    global cycle
    if used[v] == 2:
        return
    used[v] = 1
    for element in smejn[v]:
        if not cycle:
            if used[element] == 0:
                p[element] = v
                dfs(element)
            else:
                if used[element] == 1 and element != p[v]:
                    cycle = True
                    p[element] = v

                    global go
                    go = element
                    b.append(p[go])
                    go = p[go]
                    try:
                        while p[go] != v:
                            b.append(p[go])
                            go = p[go]
                        break
                    except:
                        pass

    used[v] = 2
    p.pop(v)


for i in range(1, n + 1):
    if not cycle and used[i] != 1:
        p[i] = -1
        dfs(i)
    else:
        break

if cycle:
    print("YES")
    print(len(b))
    print(' '.join(map(str, b)))
else:
    print("NO")
