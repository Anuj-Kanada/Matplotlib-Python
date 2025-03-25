# you can use argument marker to emphasize each point with specifide marker.

import matplotlib.pyplot as plt
import numpy as np 

# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, marker = 'o')
# plt.show()

'''xpoints = np.array([3, 8, 1, 10])
plt.plot(xpoints, marker = '*')
plt.show()'''

"""
# Format Strings (FMT) - marker|line|colour

ypoints = np.array([3,8,1,10])
plt.plot(ypoints, 'o:r', )
plt.show()

# line Reference
# - solid line
# : dotted line
# -- dashed line
# -. dashline/dotted line

# color reference
# b - blue
# g - green
# r - red
# w - white
# k - black
# y - yellow
# m - magenta
# c - cyan
"""
'''
# marker size (ms)
# marker edge colour (mec)
# marker face colour (mfc)
ypoints = ([3, 8, 1, 10])
plt.plot(ypoints, marker='o', mfc = 'y' ,mec = 'r' ,ms=20)
plt.show()

'''
# colour hashed value and name allowed
ypoints = ([3, 8, 1, 10])
plt.plot(ypoints, marker='o', mfc = '#33e6ff' ,mec = 'hotpink' ,ms=20)
plt.show()
