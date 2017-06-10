import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interp
import scipy.integrate as integrate

import sys
N = int(sys.argv[1])
x, y = np.mgrid[0:1:N*1j, 0:1.5:N*1j]
vx = -1 - x**2 + y
vy = 1 + x - y**2

p0 = (0.5,0.5)
dt = 0.1
t0 = 0
t1 = 1
t = np.arange(t0,t1+dt,dt)

import timeit
"""
xyarr = zip(x.flatten(),y.flatten())
vx_= vx.flatten()
vy_ = vy.flatten()


# Interpolate using griddata (only local)
start1 = timeit.time.time()

def f(p,t): 
    return [interp.griddata(xyarr,vx_,p)[0], interp.griddata(xyarr,vy_,p)[0]]

streamline1=integrate.odeint(f,p0,t)

end1 = timeit.time.time()
"""

# Interpolate using interp2d (entire field)
start2 = timeit.time.time()
dfunx = interp.interp2d(x[:],y[:],vx[:],kind='linear')
dfuny = interp.interp2d(x[:],y[:],vy[:],kind='linear')
dfun = lambda xy,t: [dfunx(xy[0],xy[1])[0], dfuny(xy[0],xy[1])[0]]

streamline2=integrate.odeint(dfun,p0,t)
end2 = timeit.time.time()

# show simulation time for both interpolation schemes
print end2-start2#end1-start1, end2-start2

#plot it
plt.figure()
#plt.plot(streamline1[:,0],streamline1[:,1])
plt.axis('equal')
#plt.hold('on')
plt.plot(streamline2[:,0],streamline2[:,1])
plt.legend(['gridata','interp2d'])
mymask = (streamline2[:,0].min()*0.9<=x) & (x<=streamline2[:,0].max()*1.1) & (streamline2[:,1].min()*0.9<=y) & (y<=streamline2[:,1].max()*1.1)
plt.quiver(x[mymask],y[mymask],vx[mymask],vy[mymask])
plt.show()

