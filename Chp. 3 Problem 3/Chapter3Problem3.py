#INSTRUCTIONS: Run the program it will print two arrays the first of which is the heights the second of which is the times that correspond to those heights
import numpy as np
#define an array of the heights from 10-0.5 every half meter
height = np.arange(10, 0, -0.5)
#defines an array of times that correspond to the heights in the height array
time = np.sqrt(2*(10-height)/9.8)
#prints the arrays
print height
print time
