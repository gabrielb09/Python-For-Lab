#INSTRUCTIONS: Run the program, input the values as requested
#creates a function for detirminting V given O, a, and Z
def eq (O,a,z):
    V=O*(1-(z/(((a**2)+(z**2))**0.5)))
    return V
#requests an O value
O = float(raw_input("Please input Vo: "))
#requests an a value
a = float(raw_input("Please input a: "))
#requests a z value
z = float(raw_input("please input z: "))
#prints the answer to the given set of conditions 
print("the answer is: V=" + str(eq(O,a,z)))
