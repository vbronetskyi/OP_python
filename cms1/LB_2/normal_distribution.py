import math

x = float(input())    
μ = float(input())    #математичне сподівання
o = float(input())    #стандартне відхилення
f = (1/math.sqrt(2*math.pi*o**2)) * math.e ** -(((x-μ)**2)/(2*o**2))

print(round(f, 10))