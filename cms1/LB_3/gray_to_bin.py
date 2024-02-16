code = input()
bin = str(int(code[0]) ^ 0) 

for i in range(1, len(code)):
    bin += str(int(code[i]) ^ int(bin[i - 1]))

print(bin)