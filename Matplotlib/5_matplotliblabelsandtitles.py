'''# Create lables and titles for plots.

import matplotlib.pyplot as plt
import numpy as np 

x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])
plt.plot(x,y)
plt.title("Health Monitor")
plt.xlabel('Average Oxyzen')
plt.ylabel("Our Calories")
plt.show()'''


'''
# now we will set the font propert for the title and labels

import matplotlib.pyplot as plt
import numpy as np 


x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])

font1 = {'family':"serif",'color':'blue','size':20}
font2 = {'family':"arial",'color':'red','size':15}

plt.plot(x,y)

plt.title("Health Monitor", fontdict=font1)
plt.xlabel('Average Oxyzen',fontdict=font2)
plt.ylabel("Our Calories", fontdict=font2)

plt.show()'''


#Change the location of title via "LOC" (Default is Center)

import matplotlib.pyplot as plt
import numpy as np 

x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])


plt.plot(x,y)
plt.title("Health Monitor", loc='left')
plt.xlabel('Average Oxyzen', loc='right')
plt.ylabel("Our Calories")
plt.show()