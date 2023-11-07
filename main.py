import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 50)
y = np.cos(x)
y2 = np.sin(x)
plt.axis([0,2 * np.pi,-1.1,1.1])
plt.xlabel('Ось х')
plt.ylabel('Ось y')
plt.title('Graf')
plt.plot(x, y, label='cos(x)')
plt.plot(x, y2, label='sin(x)')
plt.legend(loc='lower left')
plt.grid()
plt.show()
