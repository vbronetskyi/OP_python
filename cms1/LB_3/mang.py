from string import ascii_uppercase
from string import ascii_lowercase

ch1 = input()
ch2 = input()
solut = None
flg1 = False
flg2 = False

for i in range(26):
    if (ch2 == ascii_uppercase[i]) or (ch2 == ascii_lowercase[i]):
        flg2 = True
    elif (ch1 == ascii_uppercase[i]) or (ch1 == ascii_lowercase[i]):
        flg1 = True
if (flg1 & flg2):
    for i in range(26):
        if (ch2 == ascii_uppercase[i]) or (ch2 == ascii_lowercase[i]):
            solut = True
            break
        elif (ch1 == ascii_uppercase[i]) or (ch1 == ascii_lowercase[i]):
            solut = False
            break


print(solut)
