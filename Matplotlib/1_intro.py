import matplotlib
import matplotlib.pyplot as plt
import numpy as np


print(matplotlib.__version__)

xpointa = np.array([0,6])
ypointa = np.array([0,266])

plt.plot(xpointa, ypointa)
plt.show()