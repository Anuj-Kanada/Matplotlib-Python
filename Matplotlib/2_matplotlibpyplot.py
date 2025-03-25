import matplotlib
import matplotlib.pyplot as plt
import numpy as np


# plotting x and y
# plot() function is used to draw point or markers in a diagram
# there are 2 parameters for specifying points in the diagram i.e x-axis and y-axis.
 
# xpoints = np.array([1,10])
# ypoints = np.array([1,10])
# plt.plot(xpoints, ypoints, 'o')
# plt.show()

# xpoints = np.array([1,2,6,8])
# ypoints = np.array([3,8,1,10])
# plt.plot(xpoints, ypoints, 'o-')
# plt.show()

# Default X-Points
# if we do not specify the points in x axis then the default vaules 0, 1, 2, 3, 4....

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()