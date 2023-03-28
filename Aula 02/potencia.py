import numpy as np
from utils.graphs import plot

t = np.linspace(0,20)
x = np.sin((np.pi*t)/10)
plot(range = t, data = x, title='Sinal', x_label='Amostras', y_label='Valores', save_path='../images/potencia.png',)