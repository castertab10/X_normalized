import numpy as np
X = np.random.random((5,5))
print('The Original Matrix is: ',X)
standardDev = X.std()
mean = X.mean()
z = (X - mean)/standardDev
print('The Normalized Matrix is: ', mean)
np.save('X_normalized.npy', z)