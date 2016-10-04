import numpy as np
import matplotlib.pyplot as plt
def Position (jounce,j,a,v,x,t):
    X = x+(v*t)+0.5*a*(t**2)+(j*(t**3))/6 + (jounce*(t**4)/12)
    return X
def Velocity (jounce,j,a,v,t):
    V = v+a*t+(0.5*j*(t**2))+(jounce*(t**3)/6)
    return V
def Acceleration (jounce,j,a,t):
    A = a+j*t+(0.5*jounce*(t**2))
    return A
jounce = eval(raw_input("input the jounce in meters per second per second per second per second: "))
j = eval(raw_input("input the jerk in meteres per second per second per second: "))
a = eval(raw_input("input the acceleration in meters per second per second: "))
v = eval(raw_input("input the initial veloicty in meters per second: "))
x = eval(raw_input("input the initital position in meters: "))
t = eval(raw_input("input the total time elapsed in seconds: "))
Pos = [Position(jounce,j,a,v,x,0)]
Vel = [Velocity(jounce,j,a,v,0)]
Acc = [Acceleration(jounce,j,a,0)]
T = [0]
c = 1
while c < 100*t:
    Pos = Pos+[Position(jounce,j,a,v,x,(0.01*c))]
    Vel = Vel+[Velocity(jounce,j,a,v,(0.01*c))]
    Acc = Acc+[Acceleration(jounce,j,a,0.01*c)]
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
