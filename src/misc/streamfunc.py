import numpy as np
import scipy.integrate as sc
import numpy.linalg as nplin

class streamfunc:
    """ 
    A class for finding streamlines for given initial data.
    """
    def __init__(self, data):
        self.data = data 

    def find_eigen(self,T):
        dim = T.shape[0]
        eig_data =  nplin.eig(T)
        eig_values = eig_data[0]
        v1 = eig_data[1][:,0]
        v2 = eig_data[1][:,1]

        if dim == 3:
            v3 = eig_data[1][:,2]
            return eig_values,v1,v2,v3
        else:
            return eig_values,v1,v2

    def plot_streamlines(self):
        import matplotlib.pyplot as plt
        u,v = self.data
        Nx = u.shape[0]
        Ny = u.shape[1]
        x, y = np.meshgrid(np.linspace(0,Nx,Nx),np.linspace(0,Ny,Ny))

        speed = np.sqrt(u*u + v*v)
        print "plotting streamlines"
        plt.streamplot(x, y, v, u, color=u, linewidth=2, cmap=plt.cm.autumn)
        plt.colorbar()

        #f, (ax1, ax2) = plt.subplots(ncols=2)
        #ax1.streamplot(x, y, u, v, density=[0.5, 1])

        #lw = 5*speed/speed.max()
        #ax2.streamplot(x, y, u, v, density=0.6, color='k', linewidth=lw)

        plt.show()

def _read_data(key):
    """
    Returns pre-existing data from folder data.
    """
    if key == 'double_point_load':
        filename = 'data/double_point_load/doublePushPullStrain.vtk'
        u = np.loadtxt(filename,skiprows=13)
        u = u.reshape((3*16,8,3*16))
    elif key == 'isabel':
        filename = 'data/weather/isabel_2d.h5'
        import h5py as h5
        f = h5.File(filename,"r")
        ux_ = f["/Velocity/X-comp"]
        uy_ = f["/Velocity/Y-comp"]
        dim = 500
        ux = uy = np.zeros([dim,dim],dtype=np.float32)
        uy[:,:] = ux_[:,:]
        ux[:,:] = uy_[:,:]
        u = np.array([ux,uy])
    elif key == 'metsim':
        filename = 'data/weather/metsim1_2d.h5'
        import h5py as h5
        f = h5.File(filename,"r")
        ux_ = f["/Velocity/X-comp"]
        uy_ = f["/Velocity/Y-comp"]
        dim = 127
        ux = uy = np.zeros([dim,dim],dtype=np.float32)
        ux[:,:] = ux_[:,:]
        uy[:,:] = uy_[:,:]
        u = np.array([ux,uy])
    else:
        print 'Did not find any data for keyword : %s'%key
        return None
    return u

"""
import streamfunc as sf
import degenerecies as dg
import numpy as np
S = sf.streamfunc(data=None)
T = dg.T1
print S.find_eigen(T([.5,.5]))
x = y = np.linspace(-1,1,1001)
U = np.zeros([3,2,x.shape[0],y.shape[0]])
for i in range(0,x.shape[0]):
    for j in range(0,y.shape[0]):
        U[:,:,i,j] = S.find_eigen(T([x[i],y[j]]))
"""
