import numpy as np 

z = np.array([10,11,12,13,14])
nz = 5
z0 = np.zeros(len(z) + len((z)-1)*(nz))
z0[::nz+1] = z
print(z0)
