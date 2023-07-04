from utils import functions as Functions
from utils import graphs as Graphs
import numpy as np
import matplotlib.pyplot as plt
import control.matlab as co

def compensadorS(alpha, tau, ganho):
    s = Functions.s()
    return ganho * (tau*s + 1) / (alpha*tau*s + 1)


s = Functions.s()

Gp    = 10 / (0.2*s**2 + s)

alpha = [0.3,0.6,0.9]    
tau   = [1,5,10]
ganho = [1,10,15] 


compensadores = {
    "alpha" : {},
    "tau"   : {},
    "ganho" : {}
}

for a in alpha: # Alpha fixo, tau fixo, ganho variando
    compensadores["alpha"][a] = {}
    compensadores["alpha"][a]['tau'] = {}
    for t in tau:
        compensadores["alpha"][a]['tau'][t] = []
        for g in ganho:
            compensadores["alpha"][a]['tau'][t].append({
                "nome": "Ganho",
                "variacao" : g,
                "compensador": compensadorS(a, t, g)})

for a in alpha: # Alpha fixo, ganho fixo, tau variando
    compensadores["alpha"][a]['ganho'] = {}
    for g in ganho:
        compensadores["alpha"][a]['ganho'][g] = []
        for t in tau:
            compensadores["alpha"][a]['ganho'][g].append({
                "nome": "Tau",
                "variacao" : t,
                "compensador": compensadorS(a, t, g)})

for g in ganho: # ganho fixo, tau fixo, alpha variando
    compensadores["ganho"][g] = {}
    compensadores["ganho"][g]['tau'] = {}
    for t in tau:
        compensadores["ganho"][g]['tau'][t] = []
        for a in alpha:
            compensadores["ganho"][g]['tau'][t].append({
                "nome": "Alpha",
                "variacao" : a,
                "compensador": compensadorS(a, t, g)})

for g in ganho: # ganho fixo, alpha fixo, tau variando
    compensadores["ganho"][g]['alpha'] = {}
    for a in alpha:
        compensadores["ganho"][g]['alpha'][a] = []
        for t in tau:
            compensadores["ganho"][g]['alpha'][a].append({
                "nome": "Tau",
                "variacao" : t,
                "compensador": compensadorS(a, t, g)})

for t in tau: # tau fixo, alpha fixo, ganho variando
    compensadores["tau"][t] = {}
    compensadores["tau"][t]['alpha'] = {}
    for a in alpha:
        compensadores["tau"][t]['alpha'][a] = []
        for g in ganho:
            compensadores["tau"][t]['alpha'][a].append({
                "nome": "Ganho",
                "variacao" : g,
                "compensador": compensadorS(a, t, g)})

for t in tau: # tau fixo, ganho fixo, alpha variando
    compensadores["tau"][t]['ganho'] = {}
    for g in ganho:
        compensadores["tau"][t]['ganho'][g] = []
        for a in alpha:
            compensadores["tau"][t]['ganho'][g].append({
                "nome": "Alpha",
                "variacao" : a,
                "compensador": compensadorS(a, t, g)})


periodoT = 0.2
response_range = np.arange(0, 10, 0.2)
input_signal = Functions.step(response_range)
Gpz = Functions.stoz(Gp, periodoT)

for principal in compensadores.keys(): # alpha, tau, ganho
    for secundario in compensadores[principal].keys(): # Numero
        for terciario in compensadores[principal][secundario]: # alpha, tau, ganho
            for quaternario in compensadores[principal][secundario][terciario]: # Numero
                nome = ""
                for dado in compensadores[principal][secundario][terciario][quaternario]:
                    nome = dado['nome']
                    compensador = Functions.stoz(dado['compensador'], periodoT)
                    ftmf = (Gpz * compensador) / (1 + Gpz * compensador)
                    y, t, _ = Functions.response(ftmf, input_signal, response_range)
                    plt.plot(t,y, label=dado['variacao'])
                plt.legend()        
                plt.grid()
                plt.title(f'Variação {nome} \n {principal}({secundario}), {terciario}({quaternario})')
                plt.savefig("ex05/atraso/" + f'{nome}__{principal[0]}({secundario})__{terciario[0]}({quaternario})' + ".png")
                plt.clf()

                for dado in compensadores[principal][secundario][terciario][quaternario]:
                    compensador = Functions.stoz(dado['compensador'], periodoT)
                    ftmf = (Gpz * compensador) / (1 + Gpz * compensador)
                    
                    co.bode(ftmf, label=dado['variacao'])
                plt.show()

                plt.legend()
                plt.grid(True)
                plt.savefig("ex05/atraso/" + f'{nome}__{principal[0]}({secundario})__{terciario[0]}({quaternario})_bode' + ".png")
                plt.clf()

                    
           
