import numpy as np

def smooth_decay(x_max, x_min, x): 
    assert(x_min <x_max), "Error in bump.py: x_min >=x_max"
    if(x_max == x_min):
        x_min = x_min - 0.000001
    
    relx = (x- x_min)/(x_max-x_min)
    if(relx> 0.999999):
        relx = 0.999999
    if(relx<0.000001):
        relx = 0.000001
    
    return np.e**(2*np.e**(-1.0/relx)/ (relx-1))
