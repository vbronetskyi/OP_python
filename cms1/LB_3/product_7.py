n = int(input())
sum = 1

for i in range(1, n+1):
    if i%7:
        sum *= i

print(sum)