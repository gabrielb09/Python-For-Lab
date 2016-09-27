import numpy as np
#define an array of the heights from 10-0.5 every half meter
height = np.arange(10, 0, -0.5)
DeltaHeight = np.arange(9.5, -0.5, -0.5)
#defines an array of times that correspond to the heights in the height array
time = np.sqrt(2*(10-height)/9.8)
deltaT = np.sqrt(2*(10-DeltaHeight)/9.8)
averageV = -0.5/(deltaT - time)
print averageV
