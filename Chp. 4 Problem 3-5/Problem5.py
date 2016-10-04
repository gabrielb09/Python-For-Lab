#INSTRUCTIONS: run the program, it will create a text file that is the output. Make sure the text file is in same directory as the prgoram
import numpy as np
f, a, da = np.loadtxt("Data.txt", skiprows=3, unpack=True)
np.savetxt('Problem5Output.csv', zip(f, a, da),fmt="%0.16e", delimiter = ",")
