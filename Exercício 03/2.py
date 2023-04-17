import matplotlib.pyplot as plt
import control
import utils.graphs as Graphs 
import scipy.signal as sig
import control.matlab as ct
import numpy as np

z = control.TransferFunction.z  #criando a função de transferencia em Z
H = (5*z**(-1)+2*z**(-2))/(1+3*z**(-1)+2*z**(-2))

t = np.arange(0, 121, 1) 
u = 5 * sig.square(2*np.pi*0.05*t, duty=0.5) # Definição de onda genérica
y, t, _ = ct.lsim(H, u, t)


Graphs.plot(
    save_path='../images/Exercicio3b',
    multiline=True,
    grid=True,
    title='Questão 2',
    overlapping=True,
    data = [
        {
            'data'    : u,
            'range'   : t,
            'discret' : True,
            'title'   : 'Onda quadrada',
            'label'   : 'Entrada'
        },
        {
            'data'    : y,
            'range'   : t,
            'discret' : True,
            'title'   : 'Resposta a uma onda quadrada',
            'label'   : 'Resposta'
        },
    ]
)

#Polos e zeros
p, z = control.pzmap(H, Plot=False)
Graphs.pzplot(p,z)

print(f"Polos: {p}")
print(f"Zeros: {z}")
