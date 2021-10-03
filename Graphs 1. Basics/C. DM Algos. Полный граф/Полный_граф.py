n, m = [int(x) for x in input().split()]
numbers = [input().split() for i in range(int(m))]
unique_data = [list(x) for x in set(tuple(x) for x in numbers)]

new_mas = []
for i in range(1, n):
    for j in range(2, n + 1):
        if i != j and j > i:
            new_mas.append([str(i), str(j)])

if sorted(new_mas) == sorted(unique_data):
    print('YES')
else:
    print('NO')
