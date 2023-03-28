import numpy as np
from utils.graphs import plot
from utils.functions import step

t = np.linspace(-5,50)
u = step(t)
plot(
    save_path='../images/degrau.png',
    title="Degrau unitário", 
    x_label='n', 
    y_label='x[n]',
    range=t,
    data=u
)