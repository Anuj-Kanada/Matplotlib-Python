import matplotlib.pyplot as plt                      
import numpy as np 

'''
y = np.array([10,20,30,40])
mylabels = ['Apple','banana','cheery','mango']
plt.pie(y, labels=mylabels)
plt.show()
'''
# startangel - default start angel is at x-axis but you cand change the startangle by specigying startangle parameteres
# startangle = 0 - start angle in degrees, default is 0.0

'''y = np.array([10,20,30,40])
mylabels = ['Apple','banana','cheery','mango']
plt.pie(y, labels=mylabels, startangle=90)
plt.show()'''

#how to explode the piechart by a value also use of shadow parameter

'''y = np.array([10,20,30,40])
mylabels = ['Apple','banana','cheery','mango']

myexplode = [0,0,0.3,0]
mycolors = ['black','hotpink', 'b', '#4CAF50']

plt.pie(y, labels=mylabels, explode=myexplode, shadow=True,colors=mycolors)
plt.show()'''

# we can also add legenr - list of explanation
'''
y = np.array([10,20,30,40])
mylabels = ['Apple','banana','cheery','mango']
plt.pie(y, labels=mylabels)
plt.legend()
plt.show()
'''
#now we will add legend with header

y = np.array([10,20,30,40])
mylabels = ['Apple','banana','cheery','mango']
plt.pie(y, labels=mylabels)
plt.legend(title='Fruits', loc='upper left')
plt.show()