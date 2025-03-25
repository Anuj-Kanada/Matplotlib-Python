# now we will create Bars bar()

import matplotlib.pyplot as plt              
import numpy as np                       

'''#vertival bar

x =np.array(["A","B","C","D"])
y = np.array([3,8,1,10])

plt.bar(x,y)
plt.show()'''

'''# Horizontal bar

x =np.array(["A","B","C","D"])
y = np.array([3,8,1,10])

plt.barh(x,y)
plt.show()'''

'''# # color of the bar() and barh()

x =np.array(["A","B","C","D"])
y = np.array([3,8,1,10])

plt.bar(x,y,color='red')
plt.show()
'''

# # how to change bar width

# x =np.array(["A","B","C","D"])
# y = np.array([3,8,1,10])

# plt.bar(x,y, width= 0.1)
# plt.show()

# for horizontal bar used height instead of width

x =np.array(["A","B","C","D"])
y = np.array([3,8,1,10])

plt.barh(x,y, height=0.1)
plt.show()