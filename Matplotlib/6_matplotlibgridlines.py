import matplotlib.pyplot as plt 
import numpy as np 

'''
# Adding the gridlines to the plots via "grid()"

x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])

font1 = {'family':"serif",'color':'blue','size':20}
font2 = {'family':"arial",'color':'red','size':15}

plt.plot(x,y)
plt.title("Health Monitor",fontdict=font1)
plt.xlabel('Average Oxyzen', fontdict=font2)
plt.ylabel("Our Calories",fontdict=font2)
plt.grid( )
plt.show()

'''
'''# now we will specify which grid lines to display via x-axis or y-axis
# legal values are both x and y, default value is both

x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])

font1 = {'family':"serif",'color':'blue','size':20}
font2 = {'family':"arial",'color':'red','size':15}

plt.plot(x,y)
plt.title("Health Monitor",fontdict=font1)
plt.xlabel('Average Oxyzen', fontdict=font2)
plt.ylabel("Our Calories",fontdict=font2)
plt.grid(axis='x  ')
plt.show()'''


# setting up the line property

x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])

font1 = {'family':"serif",'color':'blue','size':20}
font2 = {'family':"arial",'color':'red','size':15}

plt.plot(x,y)
plt.title("Health Monitor",fontdict=font1)
plt.xlabel('Average Oxyzen', fontdict=font2)
plt.ylabel("Our Calories",fontdict=font2)
plt.grid(color='orange', ls = '--', lw='0.5' )
plt.show()