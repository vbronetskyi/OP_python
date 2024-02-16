import matplotlib.pyplot as plt
import numpy as np
import math as m
from scipy import interpolate

x,y = np.loadtxt(r"C:\Users\Admin\Desktop\12.dat", unpack = True)

x1 = x[0:-1:50]
y1 = y[0:-1:50]
a, b = 0, 5

plt.plot(x,y,color='black', label = 'Точна функція')

f1 = interpolate.interp1d(x1,y1, kind = 'zero', bounds_error = False)
f2 = interpolate.interp1d(x1,y1, kind = 'linear', bounds_error = False)
f3 = interpolate.interp1d(x1,y1, kind = 'slinear', bounds_error = False)
f4 = interpolate.interp1d(x1,y1, kind = 'quadratic', bounds_error = False)
f5 = interpolate.interp1d(x1,y1, kind = 'cubic', bounds_error = False)
x2 = np.linspace(a, b, 200)

y_new1 = f1(x2)
y_new2 = f2(x2)
y_new3 = f3(x2)
y_new4 = f4(x2)
y_new5 = f5(x2)

plt.plot(x2, y_new1, '--', label='Нульова апроксимація')
plt.legend(bbox_to_anchor=(1, 1))
plt.plot(x1, y1, 'ro')
plt.show()

plt.plot(x,y,color='black', label = 'Точна функція')
plt.plot(x2,y_new2, '--', label = 'Лінійна апроксимація')
plt.legend(bbox_to_anchor=(1.5, 1))
plt.plot(x1,y1,'ro')
plt.show()

plt.plot(x,y,color='black', label = 'Точна функція')
plt.plot(x2,y_new3, '--', label = 'Сплайн-лінійна апроксимація')
plt.legend(bbox_to_anchor=(1, 1))
plt.plot(x1,y1,'ro')
plt.show()

plt.plot(x,y,color='black', label = 'Точна функція')
plt.plot(x2,y_new4, '--', label = 'Квадратична апроксимація')
plt.legend(bbox_to_anchor=(1, 1))
plt.plot(x1,y1,'ro')
plt.show()

plt.plot(x,y,color='black', label = 'Точна функція')
plt.plot(x2,y_new5, '--', label = 'Кубічна апроксимація')
plt.legend(bbox_to_anchor=(1.5,1))
plt.plot(x1,y1,'ro')
plt.show()
