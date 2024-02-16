from scipy import constants
import math 

m = int(input())     #Маса
u = int(input())     #Швидкість
c = constants.c        #Швидкість світла

mr = m / (math.sqrt(1-(u**2/c**2)))
E = mr * c**2

print(E)