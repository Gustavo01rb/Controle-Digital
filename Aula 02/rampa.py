import numpy as np
from utils.functions import ramp
from utils.graphs import plot

t = np.linspace(-1,50,52)
u = ramp(t)

plot(range =  t, data = u, title='Rampa Unitária', x_label='n', y_label='x[n]', save_path='../images/rampa.png')