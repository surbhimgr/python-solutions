import numpy as np
import matplotlib.pyplot as plot
from matplotlib import style
from statistics import mean

#define style component
style.use('ggplot')

#defining datasets in form of array
x_dataset = np.array([1,2,3,4,5,6])
y_dataset = np.array([3,7,5,1,9,7])

# equation of line is y=mx+c and here c = mean(y)- mean(x*y) / (mean(x))^2 - mean(x^2)
def slope():
    m=(((mean(x_dataset)*mean(y_dataset))-(mean(x_dataset*y_dataset)))/((mean(x_dataset)*mean(x_dataset))-mean(x_dataset*x_dataset)))
    return m

# for calculating intercept
def intercept():
    c = mean(y_dataset) - (slope()*mean(x_dataset))
    return c

m = slope()
c = intercept()

# equation for line
regression_line = [((m*x)+c)for x in x_dataset]

# plotting the line and points
plot.scatter(x_dataset, y_dataset)
plot.plot(x_dataset, regression_line)
plot.show()