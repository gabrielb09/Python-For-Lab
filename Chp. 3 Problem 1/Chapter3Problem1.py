#all you have to do is run the program it will print out the original array first, then the array with each element squared, then the array doubled via addition, and finally the array doubled via multiplication
import numpy as np
#create the array with evenly spaced numbers 0-29 inclusive
r = np.linespace(0,29,9)
#print initial array
print r
#square the initial array and asign values to new array
rSquared = r**2
#print the squared array
print rSquared
#double array by adding to itslef
rDouble = r+r
#print doubled array
print rDouble
#double array by multiplying by two
rTimesTwo = r*2
#print doubled array
print rTimesTwo
