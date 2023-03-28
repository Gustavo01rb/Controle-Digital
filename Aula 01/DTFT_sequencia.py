import numpy as np
import matplotlib.pyplot as plt
from utils.graphs import discret_plot

n = np.arange(10)
x = np.append(1, np.zeros(9))

print(f'x[n] = {x}')

K = 4
k = np.linspace(0, 4.01, 101)
W = k * 2 * np.pi / K
X = x @ np.exp(1j * np.outer(n, W))
print('DTFT, x[n] =', X)

X_mag = abs(X)
X_phase = np.angle(X)  

discret_plot(np.flip(W), X_mag, title='Módulo', x_label='Omega', y_label='Magnitude')
discret_plot(np.flip(W), X_phase, title='Zero Fase', x_label='Omega', y_label='Angulo')