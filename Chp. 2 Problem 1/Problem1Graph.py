#INSTRUCTIONS: run the program than input the values as it asks for them, press enter to submit a value
import numpy as np
import matplotlib.pyplot as plt
#creates a function for calculating the Height and Velocity of the projectile
def HandV (h,v,t):
    #calculates Height based on initial height, velocity, and time
    H = h + (v*t) - 4.9*(t**2)
    #calculates Velocity based on initial height, velocity, and time
    V = v -9.8*t
    #returns Height and Velocity
    return (H,V)
#requets for an input for the initial height
h = eval(raw_input("input the initial height in meters: "))
#requests for an input for the initial velocity
v = eval(raw_input("input the initial velocity in meters per second: "))
#requests for an input for the total time
t = eval(raw_input("input the time elapsed in seconds: "))
#creates a list with the initial height value
H = [HandV(h,v,0)[0]]
#creates a list with the initial velocity value
V = [HandV(h,v,0)[1]]
#creats a list with the initial time value
T = [0]
#creates a counter variable for the purposes of looping
counter = 1
#loops such that there are enough points to have a time reolution of 1 miliseconds
while counter < 100*t:
    #appends the height at time one milisecond after the previous point to the list of heights
    H = H + [HandV(h,v,(0.01*counter))[0]]
    #appends the velocity at time one milisecond after the previous point to the list of velocities
    V = V + [HandV(h,v,(0.01*counter))[1]]
    #appends the time that is one milisecond after the previous time to the list of times
    T = T + [0.01*counter]
    #advances the counter by one
    counter = counter+1
#creates a figure to plot the two graphs in
plt.figure(1)
#designates the position for the first graph
plt.subplot(2,1,1)
#plots the position with respect to time
plt.plot(T, H)
#labeles the respetive axis
plt.xlabel('Time (Seconds)')
plt.ylabel('Position (Meters)')
#designates the position for the second graph
plt.subplot(2,1,2)
#plots velocity with respect to time
plt.plot(T, V)
#labeles the respective axis
plt.xlabel('Time (Seconds)')
plt.ylabel('Velocity (Meters/Second)')
#dispalys the completed plots
plt.show()
