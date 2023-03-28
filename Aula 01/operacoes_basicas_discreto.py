import numpy as np

c = np.array([3.2, 41, 36, -9.5, 0])
d = np.array([1.7, -0.5, 0, 0.8, 1])

w1 = c * d
w2 = c + d
w3 = 3.5 * c

print(f'Vetor C: {c}')
print(f'Vetor D: {d}')
print(f'\nOperações')
print(f'\tMultiplicação: {w1}')
print(f'\tAdição: {w2}')
print(f'\tMudança de escala: {w3}')


