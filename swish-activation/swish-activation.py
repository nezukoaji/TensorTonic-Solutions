import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
    x=np.array(x)
    swish = 1/(1+np.exp(-x))
    result = x*swish
    return result.tolist()
    pass