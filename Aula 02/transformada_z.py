import control
from utils.graphs import plot

num = [1, 0, 1]              # numerador da função de transferência
den = [1, -1.85, 0.9]        # denominador da função de transferência
TS = 1                       # tempo de amostragem
H = control.tf(num, den, TS) # criando a função de transferência em Z


amplitude = 0.3
t_step, y_step = control.step_response(H)
y_step *= amplitude

plot(
    save_path='../images/transformada_z.png',
    multiline=True,
    title='Transformada Z',
    data = [
        {
            'data'    : control.impulse_response(H)[1],
            'range'   : control.impulse_response(H)[0],
            'discret' : False,
            'title'   : 'Resposta ao Impulso',
            'label'   : 'Impulso'
        },
        {
            'data'    : control.step_response(H)[1],
            'range'   : control.step_response(H)[0],
            'discret' : False,
            'title'   : 'Resposta ao Degrau',
            'label'   : 'Degrau'
        },
        {
            'data'    : y_step,
            'range'   : t_step,
            'discret' : True,
            'title'   : 'Resposta ao Degrau de amplitude 0.3',
            'label'   : 'Degrau 0.3'
        },
    ]
)
