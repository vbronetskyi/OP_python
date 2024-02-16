power_n = int(input())
numb = pow(5, power_n)
bin_numb = bin(numb)
hamming_weight = 0
type_numb = None

for i in range(len(bin_numb)):
    n = (numb >> i) & 1
    if n == True:
        hamming_weight+=1

if (hamming_weight % 2):
    type_numb = 'odious'
else:
    type_numb = 'evil'

print('Number', numb, 'is', type_numb, 'number. Its hamming weight is', hamming_weight, end='.')
print()