from collections import defaultdict
import sys

n, m = [int(x) for x in input().split()]
numbers = [input().split() for x in range(m)]
used = {i: False for i in range(1, n+1)}

smejn = defaultdict(list)

for number in numbers:
    if number[0] != number[1] and int(number[1]) not in smejn[int(number[0])]:
        smejn[int(number[0])].append(int(number[1]))
        smejn[int(number[1])].append(int(number[0]))

new_components = defaultdict(list)
components = []
sys.setrecursionlimit(100000)

def dfs(v):
    used[v] = True
    components.append(v)
    abc[v] = counter+1
    for element in smejn[v]:
        if used[element] == 0:
            dfs(element)


counter = 0
abc = {}
for i in range(1, n+1):
    if not used[i]:
        components.clear()
        dfs(i)
        counter += 1

print(counter)
xx = []
for i in range(1, n+1):
    xx.append(abc[i])

print(*xx)