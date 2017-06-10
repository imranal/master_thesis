import numpy as np
u,v = np.meshgrid(np.linspace(0,2*np.pi,250),np.linspace(0,2*np.pi,250))
x = np.cos(u)*np.cos(v)
y = np.sin(u)*np.cos(v)
z = np.sin(v)

from mayavi import mlab
s = mlab.mesh(x,y,z)
mlab.show()
