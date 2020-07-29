import numpy as np
import matplotlib.pyplot as plt
x = 2
y = pow (2,3)
print ('pow (2 , 3 = ', y)
teta = 3
print ('sin teta = ', np.sin(teta))
print ('cos teta= ', np.cos(teta))
meshPoints = np.linspace (-1 , 1 , 500)
print ('the 53th element of meshPoints is: ', meshPoints [53])
plt.plot(meshPoints , np.sin(2*np.pi*meshPoints))
plt.show()

