import control
from utils.graphs import plot
import scipy.signal as sig
import numpy as np
import control.matlab as ct


z = control.TransferFunction.z
H = z**(-1) + z**(-2) + z**(-3) + z**(-4)

t = np.arange(0, 121, 1) 
u = 5 * sig.square(2*np.pi*0.05*t, duty=0.5) # Definição de onda genérica
y_sq, t_sq, _ = ct.lsim(H, u, t)

plot(
    save_path='../images/Exercicio2',
    multiline=True,
    grid=True,
    title='Questão 2',
    data = [
        {
            'data'    : control.step_response(H)[1],
            'range'   : control.step_response(H)[0],
            'discret' : True,
            'title'   : 'Resposta ao Degrau',
            'label'   : 'Degrau'
        },
        {
            'data'    : y_sq,
            'range'   : t_sq,
            'discret' : True,
            'title'   : 'Resposta a uma onda quadrada',
            'label'   : 'Onda quadrada'
        },
    ]
)