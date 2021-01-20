from math import sin
from math import cos
from math import pi

x = int(input('Градусы с долями: '))

rad_x = (pi * x) / 180


print('x: ', '% 0.3f' % rad_x)
print('Синус x: ', '% 0.3f' % sin(rad_x))
print('Косинус x: ', '% 0.3f' % cos(rad_x))
print('x в квадрате: ', '% 0.3f' % rad_x ** 2)
