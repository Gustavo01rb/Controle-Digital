import numpy as np
from utils.graphs import discret_plot

x = np.arange(0,80,1)

y1 = np.sin(x*0.05* np.pi)
y2 = np.sin(x*0.15* np.pi)
y3 = np.sin(x*0.25* np.pi)
y4 = y1 + y2/3 + y3/5

discret_plot(x,y4, title="Aproximação de uma onda quadrada")