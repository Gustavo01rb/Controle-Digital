import numpy as np
from utils.graphs import discret_plot

t = np.arange(-1,1,0.01)
h = []
d = 1

for e in t:
    if e < 0:
        h.append(0)
    else:
        h.append(d)

discret_plot(t[101::], h[101::])