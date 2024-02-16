h = int(input())

for i in range(1, h+1):
    if (i<=2) or (i==h):
        for j in range(1, i+1):
            print('*', end='')  
    else:
        for j in range(1, i+1):
            if (j==i) or (j==1):
                print('*', end='')
            else:
                print(' ', end='')
    print() 