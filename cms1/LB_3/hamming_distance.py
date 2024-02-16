x, y = input().split()
x_int = int(x)
y_int = int(y)
x_bin = bin(x_int)
y_bin = bin(y_int)

k = 0

for i in range(len(x_bin)):
    a = (x_int >> i) & 1
    b = (y_int >> i) & 1
    c = a ^ b
    if c == 1:
        k += 1
print(k)