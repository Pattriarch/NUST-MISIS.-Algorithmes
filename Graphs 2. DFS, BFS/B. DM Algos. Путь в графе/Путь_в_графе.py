from collections import defaultdict

a = []
n = int(input())
numbers = [input().split() for i in range(int(n))]

for i, j in enumerate(numbers):
    for k, l in enumerate(j):
        if l == '1':
            a.append([i + 1, k + 1])

f, k = [int(x) for x in input().split()]

smejn = defaultdict(list)
for number in a:
    if number[0] != number[1]:
        smejn[int(number[0])].append(number[1])


visited = []
queue = []
parents = {}


def bfs(visited, smejn, start_pos, finish_pos):
    visited.append(start_pos)
    queue.append(start_pos)
    parents[start_pos] = -1
    while queue:
        m = queue.pop(0)
        if m == finish_pos:
            break
        for neighbour in smejn[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                parents[neighbour] = m

    result = []
    try:
        while parents[finish_pos] != -1:
            a = parents[finish_pos]
            result.append(a)
            finish_pos = a
    except:
        pass

    result.reverse()
    if (f == k):
        print(0)
    elif (len(result) == 0):
        print(-1)
    else:
        print(len(result))
        print(' '.join(map(str, result)), k)

bfs(visited, smejn, f, k)
