import numpy as np
import matplotlib.pyplot as plt
a=1
b=2
c=1
d=-3
e=3

p1 = np.array([a,b,c]).reshape((1, 3))
p2 = np.array([c,d,e]).reshape((1, 3))

point_of_intersection = np.cross(p1, p2)
print(point_of_intersection)