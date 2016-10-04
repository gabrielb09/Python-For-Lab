import numpy as np
import matplotlib.pyplot as plt
def chaos(n,A):
    X = A*n - A*(n**2)
    return X
A1 = [0.1]
A2 = [0.1]
A3 = [0.1]
A4 = [0.1]
N = [0]
c = 1
while c < 500:
    n1 = A1[c-1]
    n2 = A2[c-1]
    n3 = A3[c-1]
    n4 = A4[c-1]
    A1 = A1+[chaos(n1,1)]
    A2 = A2+[chaos(n2,2)]
    A3 = A3+[chaos(n3,3)]
    A4 = A4+[chaos(n4,4)]
    N = N + [c]
    c = c+1
plt.figure(1)
plt.subplot(2,2,1)
plt.plot(N,A1)
plt.subplot(2,2,2)
plt.plot(N,A2)
plt.subplot(2,2,3)
plt.plot(N,A3)
plt.subplot(2,2,4)
plt.plot(N,A4)
plt.show()
