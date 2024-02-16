import math

x = float(input())

COS = math.cosh(x)
EXP = (math.exp(x)+ math.exp(-x))/2
E = (math.e ** x + math.e **(-x))/2

print("COS =", round(COS, 4))
print("EXP =", round(EXP, 4))
print("E =", round(E, 4))