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
