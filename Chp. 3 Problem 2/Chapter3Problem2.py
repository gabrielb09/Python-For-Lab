#INSTRUCTION: Run program, it creates the arrays
import numpy as np
#creates the array of size 100 to hold the value 'e'
e = np.ones(100, dtype=float)
#fills the array with 'e'
e = e*np.e
#creates the array with every degree value form 0 to 360
dgree = np.linspace(0, 360, 361)
#creates the array with the raidan equivalnets of every degree from 0 to 360
rdians = dgree * ((2*np.pi)/360)
#creates an array of every number from 12 to 17 noninclusive spaced by 0.2
nonclusive = np.arange(12, 17, 0.2)
#creates an array of every number from 12 to 17 inclusive spaced by 0.2
inclusive = np.arange(12, 17.2, 0.2)
