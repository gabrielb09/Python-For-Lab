#INSTRUCTIONS: run the program, it will print the information to the command line.
import numpy as np
a = np.array([1, 3, 5, 7])
b = np.array([8, 7, 5, 4])
c = np.array([0, 9,-6,-8])
d = zip(a, b, c)
print d
e = np.array(d)
print e
print e[3, 2]
print d[3][2]
#the three arrays have, in d, been converted to tuples and stored in a new array
#in d these arrays have been stored as arrays in an array
