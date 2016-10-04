#INSTRUCTIONS: run the program, it will print the information to the command line. Make sure the text file is in same directory as the prgoram
import numpy as np
f, a, da = np.loadtxt("Data.txt", skiprows=3, unpack=True)
print ("f =\n" + str(f))
print ("a =\n" + str(a))
print ("da =\n" + str(da))
