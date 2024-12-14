import matplotlib.pyplot as plt
from itertools import count
from matplotlib.animation import FuncAnimation
import random

# create two list with empty data at initially
x = []
y = []

#take the value count every time
a = count() 

#create live plot graph function
def livePlotGraph(i):
    x.append(next(a))
    y.append(random.randint(0,20))
    plt.cla
    plt.plot(x,y)
    
#call function n times
myfunc = FuncAnimation(plt.gcf(), livePlotGraph, interval=500)
plt.show()