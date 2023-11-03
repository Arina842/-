import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 4 * np.pi, 50)
y = np.cos(x)
plt.xlabel('Ось х')
plt.ylabel('Ось y')
plt.title('COS X')
plt.plot(x, y, color='pink', marker='o')
plt.plot(x, y)
plt.show()

