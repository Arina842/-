import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 50)
y = np.cos(x)
y2 = np.sin(x)
plt.axis([0,2 * np.pi,-1.1,1.1])
plt.xlabel('Ось х')
plt.ylabel('Ось y')
plt.title('Graf')
plt.plot(x, y, color='pink', marker='o')
plt.plot(x, y)
plt.plot(x, y2, color='pink', marker='o')
plt.plot(x, y2)
plt.grid(True)
plt.show()
print('hello word')