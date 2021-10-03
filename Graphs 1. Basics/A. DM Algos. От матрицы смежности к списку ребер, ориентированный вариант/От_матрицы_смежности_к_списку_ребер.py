n = int(input())
numbers = [input().split() for i in range(n)]
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if numbers[i][j] == '1':
            print(i+1, j+1)