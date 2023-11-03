import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 4 * np.pi, 50)
y = np.cos(x)
y2 = np.sin(x)
plt.xlabel('Ось х')
plt.ylabel('Ось y')
plt.title('COS X')
plt.plot(x, y, color='pink', marker='o')
plt.plot(x, y)
plt.plot(x, y2)
plt.show()

x_list = list(range(0, 5))
y_list = [22, 17, 6, 9]
plt.plot(x_list, y_list)
plt.show()
