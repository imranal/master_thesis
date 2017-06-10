import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

N = 201
u,v = plt.meshgrid(np.linspace(0,2*np.pi,N),np.linspace(0,2*np.pi,N))
x = np.cos(u)*np.cos(v)
y = np.sin(u)*np.cos(v)
z = np.sin(v)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x,y,z)
plt.show()

N = 201
u,v = plt.meshgrid(np.linspace(0,1,N),np.linspace(-np.pi,np.pi,N))
w = np.linspace(0,2*np.pi,N)
a = 1; 
# Redefine either u,v or w to achieve different shapes
u = 1.5 # toroids
#v = 0.5 # spherical bowls
#w = 0.1 # half-planes
x = (a*np.sinh(u)*np.cos(w))/(np.cosh(u) - np.cos(v))
y = (a*np.sinh(u)*np.sin(w))/(np.cosh(u) - np.cos(v))  
z = (a*np.sin(v))/(np.cosh(u) - np.cos(v))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x,y,z)
plt.show()
