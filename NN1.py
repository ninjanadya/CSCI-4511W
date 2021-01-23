# 1 layer feed forward network
# from https://iamtrask.github.io/2015/07/12/basic-python-network/

import numpy as np

# sigmoid function
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))
    
# input data. Each row is a sample, columns correspond to input nodes.
X = np.array([  [0,0,1],
                [0,1,1],
                [1,0,1],
                [1,1,1] ])
#newX=[[2,2,1]]    
# output data
y = np.array([[0,1,1,0]]).T

# seed random numbers to make calculation deterministic (a good practice)
np.random.seed(1)

# initialize weights randomly with mean 0. Array is 3x1 since input
# data are vectors each of 3 numbers. 
syn0 = 2*np.random.random((3,1)) - 1

# run 1,000 times -- the number of iterations can be changed
for iter in range(1000):

    # forward propagation
    l0 = X
    l1 = nonlin(np.dot(l0,syn0))

    # how much did we miss?
    l1_error = y - l1
    # print('l1 error ',l1)

    # multiply how much we missed by the 
    # slope of the sigmoid at the values in l1
    l1_delta = l1_error * nonlin(l1,True)

    # update weights
    syn0 += np.dot(l0.T,l1_delta)

print("Output After Training:")
print(l1)
