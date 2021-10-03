n, m = [int(x) for x in input().split()]
numbers = [input().split() for i in range(int(m))]

output = {}
input = {}

for num in numbers:
    output[num[0]] = 0
    input[num[1]] = 0

for num in numbers:
    output[num[0]] += 1
    input[num[1]] += 1

for i in range(1, int(n)+1):
    try:
        print(input[str(i)])
    except:
        print(0)
    try:
        print(output[str(i)])
    except:
        print(0)

