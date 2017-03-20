from numpy import *
from matplotlib.pyplot import *
x=arange(0,15,.1)
y=x**4/48 - 5*x**3/16 + 49*x**2/24 - 5*x + 5
hold()
plot(x,y)
grid()
xticks(linspace(0,15,16))
yticks(linspace(0,250,251))
show()