import numpy as np
lambda1 = 2
lambda2 = -3
alpha = -1*lambda1*lambda2
beta = lambda1 + lambda2
A = np.array([[0, 1], [alpha, beta]])
eigenvals, eigenvectors = np.linalg.eig(A)
print(eigenvals)

