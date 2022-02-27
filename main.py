import matplotlib.pyplot as plt
import numpy as np
import random
step = 0.05

myFunc = lambda x : np.sin(x)

class linearFunc:
    def __init__(self, x1, x2, y1, y2):
        self.slope = (y1 - y2)/(x1 - x2)
        self.ord = y1 - self.slope * x1
    def __call__(self, x):
        return self.slope * x + self.ord
    def error(self, func, range):
        diff = func(range) - self(range)
        return max([ abs(x) for x in diff])
        pass

startingPoint = -10
endPoint = 3
maxErr = 0.1

points = list()
points.append(startingPoint)

linFunc = None 

for i in np.arange(startingPoint + step, endPoint, step):
    if linFunc is None:
        linFunc = linearFunc(points[-1], i, myFunc(points[-1]), myFunc(i))
    err = linFunc.error(myFunc, np.arange(points[-1], i, step))
    print(err)
    if err > maxErr:
        linFunc = None
        points.append(i)
        print("last point is", points[-1])

print( "Number of points ", len(points))
print(points)
XVal = np.arange(startingPoint, endPoint, step)
plt.plot(XVal, myFunc(XVal))
plt.scatter(points, myFunc(points))
plt.show()
