import numpy as np

# we need to do rectification
# in example we have 
# e=(f,0,0) 
# to G*e = (f,0,0) via 
# G = (1,0,0)
#     (0,1,0)
#     (-1/f,0,1)

e=np.array([1,1,1])
G = np.matrix([[1,0,0], [0,1,0], [-1/1, 0, 1]])
#print(np.dot(G, e)) # [1,1,0]

# ok, we have point on infiniy, now we need only to move image "down"??
G[1,2] = -1
print(np.dot(G, e)) # [1,0,0]