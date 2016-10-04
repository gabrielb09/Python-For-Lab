#INSTRUCTIONS: run the program, it will create a text file. Make sure the data file is in same directory as the prgoram
import numpy as np
f, a, da = np.loadtxt("Data.txt", skiprows=3, unpack=True)
head = ("Date: 2013-09-16")
head = head + ("\nData taken by Liam and Selena")
head = head + ("\nfrequency (Hz) 	amplitude (mm) 	amp error (mm)")
np.savetxt('Problem4Output.txt', zip(f, a, da),header=head ,fmt='%12.4f', comments = "")
