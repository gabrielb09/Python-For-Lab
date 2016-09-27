#INSTRUCTIONS: Run the program it will print the answers sequentionally
#creates a function for detirminting V given O, a, and Z
def eq (O,a,z):
    V=O*(1-(z/(((a**2)+(z**2))**0.5)))
    return V
#sets O
O = 10
# sets a
a = 2.5
#sets Z to its first value
z = 4.3333333333333333333333333333333333333
#prints the answer given the first set of conditions
print("the answer, when z = 4 1/3 is: V=" + str(eq(O,a,z)))
#prints the answer given the second set of conditions
print("the answer, when z = 8 2/3 is: V=" + str(eq(O,a,8.66666666666666666666666666)))
#prints the answer given the third set of conditions
print("the answer, when z = 13 is: V=" + str(eq(O,a,13)))
