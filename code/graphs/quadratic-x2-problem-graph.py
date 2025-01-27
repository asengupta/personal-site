import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from labellines import labelLine, labelLines

ax = plt.axes()

x = np.linspace(-5,5,50)
y = x*x

plt.grid()

plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlim(-5,5)
plt.ylim(-1,16)
# plt.xlim(-5,5)
# plt.ylim(10,16)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("$f(x)=x^2$",fontsize=10)
labelLines(plt.gca().get_lines(),align=True,fontsize=14)
plt.xlabel('x')
plt.ylabel('g(x)')

c=4
fc=y+c
plt.plot(x, fc, '-r')
plt.text(0+0.1, -c-0.1, f'G({c})')

linex = np.linspace(-5,5,10)
for intercept in range(-15,25,5):
    m=6.
    liney = m*linex + intercept
    if intercept == -5:
        plt.plot(linex, liney, 'black', linewidth=3)
    else:
        plt.plot(linex, liney, linewidth=1)
    plt.text((13.-intercept)/6, 13, str(intercept), fontsize=6)

plt.show()
# plt.close()
