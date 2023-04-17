import matplotlib.pyplot as plt
import control
import utils.graphs as Graphs 

z = control.TransferFunction.z  #criando a função de transferencia em Z
H = (1/(1-(1/(2*z))) + 1/(1+1/(3*z)))

#plota a resposta ao degrau de amplitude qualquer
amplitude = 1
t, y = control.step_response(amplitude*H)
Graphs.plot(
    data=y,
    range=t,
    title='Resposta ao degrau unitário',
    x_label='Tempo(Segundos)',
    y_label='Amplitude'
)

#Polos e zeros
p, z = control.pzmap(H, Plot=False)
Graphs.pzplot(p,z)

print(f"Polos: {p}")
print(f"Zeros: {z}")
