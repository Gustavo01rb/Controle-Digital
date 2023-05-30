from utils import functions as Functions
from utils import graphs as Graphs
import numpy as np

z = Functions.z()

# Obtém a função de transferência em Z usando a função z() do módulo Functions
tf = [
    6 / (z**2 - z + 1),
    (5 * z**(-1) + 2 * z**(-2)) / (1 + 3 * z**(-1) + 2 * z**(-2))
]

time_range = np.arange(0, 121, 1)

# Gera uma onda quadrada multiplicada por 5 usando a função square_wave do módulo Functions
square_wave = 5 * Functions.square_wave(time_range)

# Itera sobre cada função de transferência em tf
for i, f in enumerate(tf):
    y, t, _ = Functions.response(f, square_wave, time_range)

    # Plota o gráfico da onda quadrada (entrada) e da resposta à onda quadrada
    Graphs.plot(
        data=[
            Graphs.PlotObject(
                data=square_wave,
                range=time_range,
                discrete=True,
                title='Onda quadrada',
                label='Entrada'
            ),
            Graphs.PlotObject(
                data=y,
                range=t,
                discrete=True,
                title='Resposta a uma onda quadrada',
                label='Resposta'
            ),
        ],
        multiline=True,
        grid=True,
        title=f'Questão {i+1}',
        overlapping=True,
        save_path=f'images/ex03/{i+1}.png',
    )

    # Obtém os polos e zeros da função de transferência f
    p, z = Functions.polos_and_zeros(f)

    # Plota o diagrama de polos e zeros
    Graphs.pzplot(p, z, save_path=f'images/ex03/{i+1}_pz.png')

    # Imprime os polos e zeros
    print(f'Polos: {p}')
    print(f'Zeros: {z}')
