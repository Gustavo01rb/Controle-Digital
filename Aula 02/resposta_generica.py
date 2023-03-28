import numpy as np
import scipy.signal as sig
import control.matlab as ct
from utils.graphs import plot

H = ct.TransferFunction([0.05, -0.05], [1,1.85,0.9], dt=1) 

t = np.arange(0, 121, 1) # 121 samples
alpha = 2 # slope
rampa = alpha * t
y, t, _ = ct.lsim(H,rampa, t)

plot(
    save_path='../images/resposta_g2.png',
    title='Resposta do sistema a uma rampa',
    x_label='Tempo(s)',
    y_label='Amplitude',
    range=t,
    data=y
)



# RESPONSE TO A SQUARE WAVE
t = np.arange(0, 121, 1) # 121 samples
u = 5 * sig.square(2*np.pi*0.05*t, duty=0.5) # generate a periodic square wave
y, t, _ = ct.lsim(H, u, t)

plot(
    save_path='../images/resposta_g1.png',
    title='Resposta do sistema a uma onda quadrada',
    multiline=True,
    overlapping=True,
    data=[
        {
            'data'  : u,
            'range' : t,
            'title' : 'Entrada',
            'label' : 'Entrada'
        },
        {
            'data'  : y,
            'range' : t,
            'title' : 'Saída',
            'label' : 'Saída',
            'marker': 'rs'
        }
    ]

)
