import numpy as np

def step(linspace, n = 0) -> np.array :
    response = np.zeros(linspace.shape)
    response[linspace >= n] = 1
    return response

def ramp(linspace, n = 0, alpha = 1) -> np.array:
    response = np.zeros(linspace.shape)
    response[linspace >= n] = alpha * linspace[linspace >= n]
    response[response < 0] = 0
    return response
