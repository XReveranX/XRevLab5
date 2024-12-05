import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
AutoMinorLocator)
import numpy as np

## 1/(1+(25*x*x))   0.6
x = np.linspace(0, 10, 100)
x0=0.6
y1=1/(1+(25*x*x))
y2=(-(50*x0)/((1+25*x0*x0)**2))*(x-x0) + 1/(1+(25*x0*x0))
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_title('Графики 1/(1+(25*x**2)) и её касательной', fontsize=16)
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.grid(which='major', linewidth=1.2)
ax.grid(which='minor', linestyle='--', color='gray', linewidth=0.5)
17
ax.plot(x, y1, c='red', label='y1 = 1/(1+(25*x**2))')
ax.plot(x, y2, label='y2 = касательная')
ax.legend()
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.tick_params(which='major', length=10, width=2)
ax.tick_params(which='minor', length=5, width=1)

plt.text(0.6, 0.1, 'Точка касания')
plt.scatter(0.6, 0.1,c='black')
plt.show()
