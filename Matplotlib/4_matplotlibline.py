# linestyle or ls - is used to change the style of the plotted line

import matplotlib.pyplot as plt
import numpy as np

'''
# line colour -c
# linewidth - lw

ypoint = np.array([3, 8, 1, 10])
plt.plot(ypoint, linestyle='dotted',c='r', lw='10') # dashed, 
plt.show()
'''

# multiple line

xpoints = np.array([3,8,1,10])
ypoints = np.array([6,2,7,11])
plt.plot(xpoints)
plt.plot(ypoints)
plt.show()