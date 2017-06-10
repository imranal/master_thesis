import numpy as np
import degenerecies as degen
#T = np.zeros([66,66,3,2]) # will raise index error
#degen.degenerate(T)
T = np.zeros([5,5,3,3,3]) # properly defined now
m,fdp = degen.degenerate(T)
if fdp < 100:
    for i in range(66):
        for j in range(66):
            for k in range(53):
                if m.value((i,j,k)) == 1:
                    print i,j,k,"\n"
