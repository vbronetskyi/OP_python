n = int(input())
solution = 0
flag = False
for i in range(1, n*2+1, 2):
    if (i == 1):
        print (i, end='/')
        print (i+1, end='')
    else:
        if flag:
            print (' +', i, end='/')
            print (i+1, end='')
            flag = False
        else:
            print (' -', i, end='/')
            print (i+1, end='')
            flag = True
print()