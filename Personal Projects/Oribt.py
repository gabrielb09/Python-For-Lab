import numpy as np
import matplotlib.pyplot as plt
#asssumptions:
#   initial velocity is perpendicular to the radius vector
#   component of velocity parallel to the radius vecotr is 0
#   ø = 0 in the cartesean coordinate ststem has no "y" component and a postive "x" value
#   using polar cooridnates to simplify problem (still complicated tho)
def Orbit (v,h,r,M,m,t,o):
    #initial position angle
    thetaNaught = 0
    #initial velocity angle
    VthetaNaught = np.pi/2
    #initiial acceleration angle
    AthetaNaught = np.pi
    #accelerations and force
    #force from gravity
    F = (6.674e-11)*(M*m)/((r+h)**2)
    #angle for graviational force
    Atheta = o + np.pi
    #acceleration due to gravity
    A = F/m
    #acceleration componenets
    angularAcceleration = A*np.sin(o)/(r+h)
    radialAcceleration = A*np.cos(o)
    #velocity angle
    Vtheta = VthetaNaught + angularAcceleration*t
    #velocity components relative to position vector
    Vperp = np.sin(Vtheta)*v
    Vparallel = np.cos(Vtheta)*v
    #conversion to angular velocity
    angularV = Vperp/(r+h)
    #1D motion
    theta = thetaNaught + angularV*t + 0.5*angularAcceleration*(t**2)
    R = (r+h) + Vparallel*t + 0.5*radialAcceleration*(t**2)
    return [R,theta]
#gather inputs
v = eval(raw_input("input the initial velocity in meters per second: "))
h = eval(raw_input("input the initial heigh above the planet surface in meters: "))
r = eval(raw_input("input the radius of the planet in meters: "))
M = eval(raw_input("input the mass of the planet in kilograms: "))
m = eval(raw_input("input the mass of the orbiting object in kilograms: "))
t =
counter = 0
if counter =0:
    o = 0
else
    o = theta

#graph
ax = plt.subplot(111, projection = 'polar')
ax.plot(theta, r, color = 'b')
ax.plot(theta, R, color = 'r')
ax.set_rmax(1.5*(r+h))
