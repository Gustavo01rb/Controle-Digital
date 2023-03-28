import numpy as np
from utils.functions import step
from utils.graphs import plot

t  = np.arange(0,20,1)
u  = (step(t,4) - step(t, 16))
u2 = 2*t - 2

u2[u2 < 0 ] = 0
u2[t>=14]   = 0

c  = np.convolve(u, u2)
tc = np.arange(0, c.shape[0])


plot(
    save_path='../images/convolucao.png',
    title='Convolução',
    multiline=True,
    overlapping=True,
    data=[
        {
            'data'  : u,
            'range' : t,
            'title' : 'Sinal 1',
            'label' : 'Sinal 1'
        },
        {
            'data'  : u2,
            'range' : t,
            'title' : 'Sinal 2',
            'label' : 'Sinal 2',
            'marker': 'bo'
        },
        {
            'data'  : c,
            'range' : tc,
            'title' : 'Convolução',
            'label' : 'Convolução',
            'marker': 'rs'
        },
    ]
)
