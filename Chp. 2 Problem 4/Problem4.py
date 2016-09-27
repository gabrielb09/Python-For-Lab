#INSTRUCTIONS: run the program input the values of a, b, and c as it is requested
import cmath
#creates a fucntion which solves for the roots of a quadratic equation of the form ax^2+bx+c
def quad (a,b,c):
    x1 = ((-1*b)+ cmath.sqrt((b**2)-(4*a*c)))/(2*a)
    x2 = ((-1*b)- cmath.sqrt((b**2)-(4*a*c)))/(2*a)
    return (x1,x2)
#gets a
a = float(raw_input("what does a equal? "))
a = a+0j
#gets b
b = float(raw_input("what does b equal? "))
b = b+0j
#gets c
c = float(raw_input("what does c equal? "))
c = c+0j
#solves the quadratic equations
quadratic = quad(a,b,c)
#prints the roots
print("The roots are: {0:0.3f} + {1:0.3f}i and {2:0.3f} + {3:0.3f}i".format(quadratic[0].real,quadratic[0].imag,quadratic[1].real,quadratic[1].imag))
