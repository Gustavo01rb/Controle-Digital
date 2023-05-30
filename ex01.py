import utils.functions as Functions
import utils.graphs as Graphs
import numpy as np

# Importa funções utilitárias de módulos externos

z = Functions.z()

# Obtém o valor de z usando a função z() do módulo Functions

ft = [
    (1/(1-(1/(2*z)))) + (1/(1+(1/(3*z)))),
    1 - (1/z),
    (1/(1 - z**(-1))) * (1/(1-z**(-1))),
    z**(-1) + z**(-2) + z**(-3) + z**(-4)
]

# Lista ft contendo expressões matemáticas envolvendo z, que representam diferentes funções

for i, f in enumerate(ft):
    time_range = np.arange(0, 121, 1) 
    square_wave = Functions.square_wave(time_range)
    step = Functions.step(time_range)
    
    # Define os intervalos de tempo, obtém uma onda quadrada e um degrau usando as funções do módulo Functions
    
    y_s, t_s, _ = Functions.response(f, square_wave, time_range)
    y, t, _ = Functions.response(f, step, time_range)
    
    # Calcula as respostas das funções f à onda quadrada e ao degrau nos intervalos de tempo especificados
    
    Graphs.plot(
        multiline=True,
        grid=True,
        title=f'Questão {i+1}',
        save_path=f'images/ex01/{i+1}.png',
        data=[
            Graphs.PlotObject(
                data=y,
                range=t,
                discrete=True,
                title='Resposta ao Degrau',
                label='Degrau'
            ),
            Graphs.PlotObject(
                data=y_s,
                range=t_s,
                discrete=True,
                title='Resposta a uma onda quadrada',
                label='Onda quadrada'
            ),
        ]
    )

    # Gera um gráfico com as respostas das funções f à onda quadrada e ao degrau e salva como imagem
