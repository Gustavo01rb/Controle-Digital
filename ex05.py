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
T_values = [0.1, 0.246,  0.366, 0.442,0.5]

# Definição dos vetores para armazenar as respostas de cada valor de T
closed_loop_responses = []
open_loop_responses = []

for T in T_values:
    time_range = np.arange(0, 50, 1) 
    input_signal = Functions.step(time_range)

    y_closed, t_closed, _ = Functions.response(closed_loop(T), input_signal, time_range)
    
    closed_loop_responses.append(        
        Graphs.PlotObject(
            data=y_closed,
            range=t_closed,
            title= f'T = {T}',
            label= f'T = {T}',
            discrete = False,
        ))

    y_open, t_open, _ = Functions.response(open_loop(T), input_signal, time_range)
    

    open_loop_responses.append(
        Graphs.PlotObject(
            data=y_open,
            range=t_open,
            title= f'T = {T}',
            label= f'T = {T}',
            discrete = False ,
        )
    )

# Plotagem dos resultados

Graphs.plot(
    multiline=False,
    data=open_loop_responses,
    title="Malha aberta",
    show=False,
    save_path="images/ex05/open_group.png"
)
Graphs.plot(
    multiline=True,
    data=open_loop_responses,
    title="Malha aberta",
    show=False,
    save_path="images/ex05/open_single.png",
)
Graphs.plot(
    multiline=False,
    data=closed_loop_responses,
    title="Malha fechada",
    show=False,
    save_path="images/ex05/close_group.png"
)
Graphs.plot(
    multiline=True,
    data=closed_loop_responses,
    title="Malha fechada",
    show=False,
    save_path="images/ex05/close_single.png",
)
