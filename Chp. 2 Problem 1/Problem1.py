#INSTRUCTIONS: run the program, it will print the information to the command line.
#creates a function for calculating the Height and Velocity of the projectile
def HandV (h,v,t):
    #calculates Height based on initial height, velocity, and time
    H = h + (v*t) - 4.9*(t**2)
    #calculates Velocity based on initial height, velocity, and time
    V = v -9.8*t
    #returns Height and Velocity
    return (H,V)
#prints the height and speed at T=0s
print("at time T=0 seconds the ball is " + str(HandV(1.2, 5.4, 0)[0]) + " meters up, and is traveling at " + str(HandV(1.2,5.4,0)[1]) + " meters per second")
#prints the height and speed at T=0.5s
print("at time T=0.5 seconds the ball is " + str(HandV(1.2, 5.4, 0.5)[0]) + " meters up, and is traveling at " + str(HandV(1.2,5.4,0.5)[1]) + " meters per second")
#prints the height and speed at T=2s
print("at time T=2 seconds the ball is " + str(HandV(1.2, 5.4, 2)[0]) + " meters up, and is traveling at " + str(HandV(1.2,5.4,2)[1]) + " meters per second")
