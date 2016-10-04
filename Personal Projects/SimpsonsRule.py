import numpy as np
def fx(x):
    FX = (1/np.sqrt(2*np.pi))*np.e**(-((x**2)/2))
    return FX
a = -1.0
b = 1.0
n = 20.0
dX = (b-a)/n
counter = 0
Simp = 0.0
while counter <= n:
    if counter == 0 or counter == n:
        temp = fx(-1+counter*dX)
    elif counter % 2 != 0:
        temp = 4*fx(-1+counter*dX)
    elif counter % 2 == 0:
        temp = 2*fx(-1+counter*dX)
    Simp = Simp+temp
    counter = counter+1
Simpsons = (dX/3)*Simp
print Simpsons
