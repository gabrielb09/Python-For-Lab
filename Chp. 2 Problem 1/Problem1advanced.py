#INSTRUCTIONS: run the program than input the values as it asks for them, press enter to submit a value
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
#computes the final Height and Velocity
answer = HandV(h,v,t)
#prints out the Height at the inputted time
print("the ball is " + str(answer[0]) + " meters up")
#prints out the velocity at the inputted time
print("the ball is moving at " + str(answer[1]) + " meters per second")
#prints out the total time elapsed
print(str(t) + " seconds have elapsed")
