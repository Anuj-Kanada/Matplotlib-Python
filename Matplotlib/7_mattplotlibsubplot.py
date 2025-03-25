# Display the multiple plots - with subplot() you can

import matplotlib.pyplot as plt 
import numpy as np 

"""x = np.array([0,1,2,3])
y = np.array([3, 8, 1, 10])
#plot1
plt.subplot(1,2,1) # the figure has 1 row 2 columns and 1 for first plot
plt.plot(x,y,'r') # plot x vs y with red color

#plot 2

x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(1,2,2)
plt.plot(x,y,'g') # plot x vs y with green color

plt.show()
"""

'''# now we will draw 2 plot on top of two other

x = np.array([0,1,2,3])
y = np.array([3, 8, 1, 10])
#plot1
plt.subplot(2,1,1) # the figure has 1 row 2 columns and 1 for first plot
plt.plot(x,y,'r') # plot x vs y with red color

#plot 2

x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(2,1,2)
plt.plot(x,y,'g') # plot x vs y with green color

plt.show()
'''

# Now we will draw a challange of six plot
#plot1
x = np.array([0,1,2,3])
y = np.array([3, 8, 1, 10])



plt.subplot(2,3,1) # the figure has 1 row 2 columns and 1 for first plot
plt.plot(x,y,'r') # plot x vs y with red color
plt.title("Sales")
#plot 2

x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(2,3,2)
plt.plot(x,y,'g') # plot x vs y with green color
plt.title("demand")
#plot3
x = np.array([0,1,2,3])
y = np.array([3, 8, 1, 10])
plt.subplot(2,3,3)
plt.plot(x,y,'k')
plt.title("Scalebility")

#plot4
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(2,3,4)
plt.plot(x,y,'y')
plt.title("Risk")
#plot5
x = np.array([0,1,2,3])
y = np.array([3, 8, 1, 10])
plt.subplot(2,3,5)
plt.plot(x,y,'b')
plt.title("IT")

#plot6
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(2,3,6)
plt.plot(x,y,'c')
plt.title("Marketing")

plt.suptitle("Strategical Analysis")
plt.show()
            
        