from math import pi
r = float(input())      #радіус
h = float(input())      #висота

V=h*pi*r**2             #площа поверхні
A=h*2*pi*r+2*pi*r**2    #об'єм

print("V =", round(V, 3))
print("A =", round(A, 3))