import matplotlib.pyplot as plt     
import numpy as np             

# The Scatter() function plot one dot for each observations.
'''
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show() 
'''

'''
# now we will comapra 2 plots on same figure

#day 1, The age and speed of 13 cars
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color='g')

#day 2, The age and speed of 13 cars

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,80,85,99])

plt.scatter(x,y,color='y')
plt.show()
'''

'''
# now we will change the colour of each dots

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = (["red","green", "yellow", "brown","pink","black","orange","purple","beige","gray","cyan","magenta","blue"])
plt.scatter(x,y, c = colors)
plt.show() '''

# now we will create a color arrsy and specify a colormap

"""x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

colors = np.array([0,10,20,30,40,45,50,55,60,70,80,90,100])

plt.scatter(x, y, c = colors, cmap='viridis')
plt.show() """

# you can also include colorbar in the plot
'''
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

colors = np.array([0,10,20,30,40,45,50,55,60,70,80,90,100])

plt.scatter(x, y, c = colors, cmap='viridis')
plt.colorbar()
plt.show() '''

'''# you can also change the size


x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

sizes = np.array([20,50,100,200,500,1000,60,60,90,10,300,600,00])

plt.scatter(x, y, s = sizes)
plt.colorbar()
plt.show()''' 

'''
#alpha is used to adjust the transparency of the dots

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

sizes = np.array([20,50,100,200,500,1000,60,60,90,10,300,600,00])

plt.scatter(x, y, s = sizes, alpha =0.5)
plt.colorbar()
plt.show() '''

# now we will combine colour , size and alpha

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colours = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))
plt.scatter(x,y,c=colours,s=sizes,alpha=0.5,cmap='nipy_spectral')
plt.colorbar()
plt.show()