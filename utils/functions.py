import numpy as np
import scipy.signal as sig
import control.matlab as ct

def z():
    """
    Retorna a função de transferência em Z.
    """
    return ct.TransferFunction.z

def s():
    """
    Retorna a função de transferência em S.
    """
    return ct.TransferFunction.s

def step(linspace, n=0) -> np.array:
    """
    Gera um sinal degrau unitário.

    Args:
        linspace (np.array): Array de tempo.
        n (float, opcional): Instante de tempo em que ocorre a transição. O padrão é 0.

    Returns:
        np.array: Sinal degrau unitário.
    """
    response = np.zeros(linspace.shape)
    response[linspace >= n] = 1
    return response

def ramp(linspace, n=0, alpha=1) -> np.array:
    """
    Gera um sinal rampa.

    Args:
        linspace (np.array): Array de tempo.
        n (float, opcional): Instante de tempo em que ocorre a transição. O padrão é 0.
        alpha (float, opcional): Coeficiente de inclinação da rampa. O padrão é 1.

    Returns:
        np.array: Sinal rampa.
    """
    response = np.zeros(linspace.shape)
    response[linspace >= n] = alpha * linspace[linspace >= n]
    response[response < 0] = 0
    return response

def square_wave(linspace):
    """
    Gera uma onda quadrada.

    Args:
        linspace (np.array): Array de tempo.

    Returns:
        np.array: Onda quadrada.
    """
    return sig.square(2 * np.pi * 0.05 * linspace, duty=0.5)

def response(transfer_function, function, linspace):
    """
    Calcula a resposta de um sistema a um determinado sinal de entrada.

    Args:
        transfer_function (TransferFunction): Função de transferência do sistema.
        function (np.array): Sinal de entrada.
        linspace (np.array): Array de tempo.

    Returns:
        np.array: Resposta do sistema ao sinal de entrada.
    """
    return ct.lsim(transfer_function, function, linspace)

def polos_and_zeros(transfer_function):
    """
    Retorna os polos e zeros de uma função de transferência.

    Args:
        transfer_function (TransferFunction): Função de transferência do sistema.

    Returns:
        None
    """
    return ct.pzmap(transfer_function, Plot=False)

def stoz(transfer_function, T):
    return ct.c2d(transfer_function, T, method='zoh')
