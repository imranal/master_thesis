import numpy as np
T = np.zeros([100,100,2,2])
for i in range(0,100):
    for j in range(0,100):
        T[i,j,:,:] = np.random.random([2,2])
# add a degenerate point at (50,51) :
T[51,50,:,:] = np.array([[2,0],[0,2]])
# add a degenerate point at (75,14) :
T[75,14,:,:] = np.array([[1,1e-8],[1e-8,1]])
import degenerecies as dg
deg_point = dg.degenerate(T) # 100x100 sparse matrix
print deg_point # prints only non-zero values, i.e the degenerate points
