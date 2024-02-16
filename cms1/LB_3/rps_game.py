sequ = []
option = "None"
while option != '':
    sequ.append(option)
    option = input()


for i in range(1, len(sequ)):
    if (sequ[i][0]=='S'and sequ[i][1]=='P')|(sequ[i][0]=='P'and sequ[i][1]=='R')|(sequ[i][0]=='R'and sequ[i][1]=='S'):
        print('True')
    elif (sequ[i][0]==sequ[i][1]):
        print('False | False')
    else:
        print('False')
