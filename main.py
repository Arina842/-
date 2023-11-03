import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 50)
y = np.cos(x)
y2 = np.sin(x)
<<<<<<< HEAD
=======
plt.axis([0,2 * np.pi,-1.1,1.1])
>>>>>>> 4f232af6531ae017f3c0217e4850c872bc635efc
plt.xlabel('Ось х')
plt.ylabel('Ось y')
plt.title('Graf')
plt.plot(x, y, color='pink', marker='o')
plt.plot(x, y)
<<<<<<< HEAD
plt.plot(x, y2)
=======
plt.plot(x, y2, color='pink', marker='o')
plt.plot(x, y2)
plt.grid(True)
>>>>>>> 4f232af6531ae017f3c0217e4850c872bc635efc
plt.show()

x_list = list(range(0, 5))
y_list = [22, 17, 6, 9]
plt.plot(x_list, y_list)
plt.show()
