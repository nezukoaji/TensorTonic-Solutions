import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x= np.array(x)
    expo_pos = np.exp(x)
    expo_neg =np.exp(-x)

    return (expo_pos -expo_neg)/(expo_pos+ expo_neg)
    pass