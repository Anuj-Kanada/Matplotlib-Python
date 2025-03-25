# Histrogram - is a graph showing the frequenscy distribution.

import matplotlib.pyplot as plt                        
import numpy as np                               

# example - say you ask fot thr height of 250 people then how we will make a histrogram
#hist()
#   func read the array andproduce the histrogram

x = np.random.normal(170,10,250)
plt.hist(x)
plt.show()