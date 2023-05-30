from utils import functions as Functions
from utils import graphs as Graphs
import numpy as np

z = Functions.z()

# Obtém a função de transferência em Z usando a função z() do módulo Functions
tf = (1/(1-(1/(2*z))) + 1/(1+1/(3*z)))

time_range = np.arange(0, 121, 1)

# Cria um sinal degrau unitário usando a função step do módulo Functions
step = Functions.step(time_range)

# Calcula a resposta do sistema representado pela função de transferência tf ao sinal degrau
y, t, _ = Functions.response(tf, step, time_range)

# Plota o gráfico da resposta ao degrau
Graphs.plot(
    data=Graphs.PlotObject(
        data=y,
        range=t,
        discrete=True,
        title='Resposta ao Degrau unitário',
        label='Degrau',
    ),
    grid=True,
    title='Questão 2',
    save_path='images/ex02/2.png',
    x_label='Tempo (s)',
    y_label='Amplitude',
)

# Obtém os polos e zeros da função de transferência tf
p, z = Functions.polos_and_zeros(tf)

# Plota o diagrama de polos e zeros
Graphs.pzplot(p, z, save_path='images/ex02/2pz.png')

# Imprime os polos e zeros
print(f"Polos: {p}")
print(f"Zeros: {z}")
