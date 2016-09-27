import numpy as np
import matplotlib.pyplot as plt
#ONLY FORCE IS GRAVITY
#USE POLAR COORDINATES
def Orbit (v,h,r,M,m,t,o):
    #force due to gravity
    F = (6.674e-11)*(M*m)/((r+h)**2)
    


