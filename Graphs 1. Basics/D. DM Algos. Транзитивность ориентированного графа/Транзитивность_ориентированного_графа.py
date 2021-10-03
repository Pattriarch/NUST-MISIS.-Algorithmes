n = int(input())
numbers = [input().split() for i in range(int(n))]
res = 1

for i in range(n):
    for j in range(n):
        if numbers[i][j] == '1':
            for k in range(n):
                if numbers[j][k] == '1' and numbers[i][k] == '0':
                    res = 0
if res == 1:
    print('YES')
else:
    print('NO')