import numpy as np
from utils.graphs import plot

t = np.arange(0,20,1)
y = np.zeros(t.shape)
y[4:16] = 1
x = y * (np.sin(2*np.pi*t/15)+1)
plot(range = t, data =  x, title='Sinal', y_label='valores', x_label='Amostras',save_path='../images/energia.png',)