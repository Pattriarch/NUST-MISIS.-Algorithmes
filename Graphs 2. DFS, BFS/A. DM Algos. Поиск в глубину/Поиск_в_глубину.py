from collections import defaultdict
import sys

n, m = [int(x) for x in input().split()]
numbers = [input().split() for x in range(m)]
used = {i: False for i in range(1, n+1)}

unique_numbers = set()
new_line = set()
smejn = defaultdict(list)

for number in numbers:
    if number[0] != number[1]:
        smejn[int(number[0])].append(number[1])
        smejn[int(number[1])].append(number[0])

sys.setrecursionlimit(2000)

def dfs(v):
    if used[v]:
        return
    used[v] = True
    for element in smejn[v]:
        dfs(int(element))
dfs(1)

ke_ys = [k for k, v in used.items() if v == True]

print(len(ke_ys))
print(' '.join(map(str, ke_ys)))
