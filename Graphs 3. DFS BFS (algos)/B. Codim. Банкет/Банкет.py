from collections import defaultdict

n, m = [int(x) for x in input().split()]
numbers = [input().split() for x in range(m)]
used = {i: 0 for i in range(1, n+1)}

smejn = defaultdict(list)

for number in numbers:
    if number[0] != number[1]:
        smejn[int(number[0])].append(int(number[1]))
        smejn[int(number[1])].append(int(number[0]))

flag = True
def dfs(v, c):
    global flag
    if flag:
        used[int(v)] = c
        for element in smejn[v]:
            if flag:
                if used[element] == 0:
                    dfs(element, 3-c)
                elif used[element] == c:
                    flag = False
                    print("NO")
                    return


for i in range(1, n):
    if flag and used[i] == 0:
        dfs(int(i), 1)

c = []
if flag:
    print("YES")
    for i in range(1, n+1):
        if used[i] == 1:
            c.append(i)
    print(' '.join(map(str, c)))