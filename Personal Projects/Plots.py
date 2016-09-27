import numpy as np
import matplotlib.pyplot as plt
def Position (a,v,x,t):
    X = x+(v*t)+0.5*a*(t**2)
    return X
def Velocity (a,v,t):
    V = v+a*t
    return V
a = eval(raw_input("input the acceleration in meters per second per second: "))
v = eval(raw_input("input the initial veloicty in meters per second: "))
x = eval(raw_input("input the initital position in meters: "))
t = eval(raw_input("input the total time elapsed in seconds: "))
Pos = [Position(a,v,x,0)]
Vel = [Velocity(a,v,0)]
Acc = [a]
T = [0]
c = 1
while c < 100*t:
    listP = [Position(a,v,x,(0.01*c))]
    listV = [Velocity(a,v,(0.01*c))]
    listA = [a]
    Pos = Pos+listP
    Vel = Vel+listV
    Acc = Acc+listA
    T = T+[0.01*c]
    c = c+1
plt.figure(1)
plt.subplot(3,1,1)
plt.plot(T, Pos)
plt.subplot(3,1,2)
plt.plot(T, Vel, color='red')
plt.subplot(3,1,3)
plt.plot(T, Acc, color='green')
plt.show()
