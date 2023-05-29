import utils.functions as Functions
import utils.graphs as Graphs
import numpy as np
from math import e

def closed_loop(T):
    """
    Calcula a função de transferência da malha fechada.

    Args:
        T (float): Valor de T.

    Returns:
        TransferFunction: Função de transferência da malha fechada.
    """
    G = open_loop(T)
    return G / (1 + G)

def open_loop(T):
    """
    Calcula a função de transferência da malha aberta.

    Args:
        T (float): Valor de T.

    Returns:
        TransferFunction: Função de transferência da malha aberta.
    """
    z = Functions.z()
    return (2 * (1 - e**(-2*T)) ) / (z - e**(-2*T))

# Definição dos valores de T
T_values = [0.1, 0.366, 0.524, 0.733, 0.98]

# Definição dos vetores para armazenar as respostas de cada valor de T
closed_loop_responses = []
open_loop_responses = []

for T in T_values:
    time_range = np.arange(0, 100, 1) 
    input_signal = Functions.step(time_range)

    y_closed, t_closed, _ = Functions.response(closed_loop(T), input_signal, time_range)
    
    closed_loop_responses.append({
        'y': y_closed,
        't': t_closed,
        'T_value': T
    })

    y_open, t_open, _ = Functions.response(open_loop(T), input_signal, time_range)
    
    open_loop_responses.append({
        'y': y_open,
        't': t_open,
        'T_value': T
    })

# Plotagem dos resultados
closed_loop_plots = []
open_loop_plots = []

for response in closed_loop_responses:
    closed_loop_plots.append(
        {
            'data': response['y'],
            'range': response['t'],
            'discret': False,
            'title': 'T = ' + str(response['T_value']),
            'label': 'Step'
        }
    )
for response in open_loop_responses:
    open_loop_plots.append(
        {
            'data': response['y'],
            'range': response['t'],
            'discret': False,
            'title': 'T = ' + str(response['T_value']),
            'label': 'Step'
        }
    )

Graphs.plot(
    multiline=True,
    grid=True,
    title='Closed-loop System',
    data=closed_loop_plots
)
Graphs.plot(
    multiline=True,
    grid=True,
    title='Open-loop System',
    data=open_loop_plots
)
