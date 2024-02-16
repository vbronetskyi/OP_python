first_numb = int(input())
parameters = int(input())

for i in range(1, parameters+1):
    p = first_numb
    for j in range(1, parameters+2-i):
        if j == parameters+1-i:
            print(p, end='')
        else:
            print(p, end=' ')
            p+=1
    print()