import numpy as np
import matplotlib.pyplot as plt

a = 0.5
n = np.arange(10)
x = np.zeros(10)

for i in range(10):
    x[i] = (a*np.exp(-1j*i*np.pi))**i  # x[n]

fator = 100

K = 4
k = np.arange(0, 4, 4/fator)  # dominio temporal t
W = k * 6 * np.pi / K
X = np.dot([x], np.exp(1j*np.outer(n, W)))  # X(ejomega)

X_mag = np.abs(X)
X_phase = np.angle(X)

fig, ax = plt.subplots()
ax.plot(np.flip(W), X_mag[0])
ax.set(xlabel='Omega w', ylabel='Amplitude',
       title='Ganho (modulo)')
ax.grid()

fig, ax = plt.subplots()
ax.plot(np.flip(W), X_phase[0])
ax.set(xlabel='Omega w', ylabel='angulo (Teta)',
       title='Fase (angulo)')
ax.grid()

fig, ax = plt.subplots()
ax.stem(n, x)
ax.set(xlabel='n (tempo discreto)', ylabel='Amplitude sinal',
       title='Amplitude sinal')
ax.grid()

plt.show()