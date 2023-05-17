import numpy as np
import pickle
import matplotlib.pyplot as plt
 
 
def softmax(x):
    """ Standard definition of the softmax function """
    return np.exp(x) / np.sum(np.exp(x), axis=0)