import matplotlib.pyplot as plt
t = [0.0]
a = [-9.8]
v = [0.0]
x = [10.0]
count = 0
while count < 21 :
    time = [count*0.1]
    t = t + time
    acceleration = [-9.8]
    a = a + acceleration
    velocity = [0.0 - 9.8*(count*0.1)]
    v = v + velocity
    position = [x[count]+v[count]*(0.1)]
    x = x + position
    count += 1
plt.plot(t, t)
plt.show()
