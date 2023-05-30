import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import matplotlib.cm as cm

def list_colors(): return ['bo','go','ro','co','mo','yo','ko','wo',]

class PlotObject:
    def __init__(self, 
                data, 
                range, 
                discrete=True, 
                marker=None, 
                label=None,
                title=None
                ):
        """
        Classe para armazenar informações de um objeto de plotagem.

        Args:
            data (array): Dados a serem plotados.
            range (array): Eixo x correspondente aos dados.
            discrete (bool, opcional): Indica se os dados são discretos. O padrão é True.
            marker (str, opcional): Marcador utilizado para plotagem discreta. O padrão é None.
            label (str, opcional): Rótulo do objeto de plotagem. O padrão é None.
            title (str, opcional): Título do objeto de plotagem. O padrão é None.
        """
        self.data = data
        self.range = range
        self.discrete = discrete
        self.marker = marker
        self.label = label
        self.title = title


def plot(data, 
        multiline=False, 
        title=None,
        x_label=None,
        y_label=None,
        font_size_label=12,
        font_size_legend=10,
        grid=True,
        show=False,
        save_path=None,
        overlapping=False):
    """
    Função para plotar dados.

    Args:
        data (list or PlotObject): Dados a serem plotados. Pode ser uma lista de objetos PlotObject ou um único objeto PlotObject.
        multiline (bool, opcional): Indica se serão plotadas várias linhas no mesmo gráfico. O padrão é False.
        title (str, opcional): Título do gráfico. O padrão é None.
        x_label (str, opcional): Rótulo do eixo x. O padrão é None.
        y_label (str, opcional): Rótulo do eixo y. O padrão é None.
        font_size_label (int, opcional): Tamanho da fonte dos rótulos dos eixos. O padrão é 12.
        font_size_legend (int, opcional): Tamanho da fonte da legenda. O padrão é 10.
        grid (bool, opcional): Indica se as linhas de grade devem ser exibidas no gráfico. O padrão é True.
        show (bool, opcional): Indica se o gráfico deve ser exibido. O padrão é False.
        save_path (str, opcional): Caminho para salvar o gráfico. O padrão é None.
        overlapping (bool, opcional): Indica se as linhas do gráfico devem se sobrepor. O padrão é False.

    Returns:
        None
    """
    plt.clf()
    if multiline:
        plot_multiline(data, overlapping, title)
    else: 
        plt.title(title if title is not None else "", fontsize=22, fontweight="bold")
        if isinstance(data, list):
            for it in data:
                plot_single(it)
        else:
            plot_single(data)
        
    plt.legend(prop={'size': font_size_legend})    
    if x_label is not None:
        plt.ylabel(y_label, fontsize=font_size_label)
    if y_label is not None:
        plt.xlabel(x_label, fontsize=font_size_label)

    plt.grid(grid)
    if save_path is not None:
        plt.savefig(save_path)
    if show:
        plt.show()


def plot_discrete(object, ax=None):
    """
    Função para plotar dados discretos.

    Args:
        object (PlotObject): Objeto contendo informações sobre os dados discretos.
        ax (AxesSubplot, opcional): Eixos em que os dados serão plotados. O padrão é None.

    Returns:
        None
    """
    plt.gca().set_prop_cycle(None)
    if ax is None:
        plt.stem(object.range, object.data, label=object.label, markerfmt=object.marker)
        return
    ax.stem(object.range, object.data, label=object.label, markerfmt=object.marker)
    

def plot_continuous(object, ax=None):
    """
    Função para plotar dados contínuos.

    Args:
        object (PlotObject): Objeto contendo informações sobre os dados contínuos.
        ax (AxesSubplot, opcional): Eixos em que os dados serão plotados. O padrão é None.

    Returns:
        None
    """
    if ax is None:
        plt.plot(object.range, object.data, label=object.label)
        return
    ax.plot(object.range, object.data, label=object.label)
    

def plot_single(object):
    """
    Função para plotar um único objeto.

    Args:
        object (PlotObject): Objeto contendo informações sobre os dados a serem plotados.

    Returns:
        None
    """
    fig = plt.figure(1)
    fig.set_figwidth(12)
    if object.discrete:
        plot_discrete(object)
        return
    plot_continuous(object)
    

def plot_multiline(data, overlapping, title):
    """
    Função para plotar várias linhas no mesmo gráfico.

    Args:
        data (list): Lista de objetos PlotObject contendo informações sobre os dados a serem plotados.
        overlapping (bool): Indica se as linhas do gráfico devem se sobrepor.
        title (str): Título do gráfico.

    Returns:
        None
    """
    fig, axs = plt.subplots(len(data) + overlapping)
    fig.tight_layout()
    fig.subplots_adjust(top=0.9)
    fig.set_figwidth(21)
    fig.set_figheight(12)

    if title is not None:
        fig.suptitle(title, fontsize=22, fontweight="bold")

    last = len(data)
    for index, it in enumerate(data):
        if not it.discrete:
            plot_continuous(it, axs[index])
            if overlapping:
                plot_continuous(it, axs[last])

        else:
            plot_discrete(it, axs[index])
            if overlapping:
                plot_discrete(it, axs[last])
        axs[index].legend()

        if index == last - 1 and overlapping:
            axs[last].legend()

        if it.title is not None:
            axs[index].set_title(it.title, loc='left', fontsize=16, fontweight=200)


def pzplot(p, z, save_path=None, show = False):
    """
    Função para plotar o gráfico de polos e zeros.

    Args:
        p (list): Lista contendo os polos.
        z (list): Lista contendo os zeros.
        save_path (str, opcional): Caminho para salvar a figura. O padrão é None.

    Returns:
        None
    """
    plt.clf()
    _, ax = plt.subplots()

    # Plota os polos e zeros
    ax.scatter(np.real(z), np.imag(z), marker='o', facecolors='none', edgecolors='b')
    ax.scatter(np.real(p), np.imag(p), marker='x', color='r')

    # Plota o círculo unitário
    unit_circle = mpatches.Circle((0, 0), 1, fill=False, linestyle='--', linewidth=0.5)
    ax.add_patch(unit_circle)
    ax.axvline(x=0, color='k', linewidth=0.5)
    ax.axhline(y=0, color='k', linewidth=0.5)

    ax.axis('equal')
    plt.title('Polos e Zeros')
    plt.grid(True)
     
    if save_path is not None: plt.savefig(save_path)
    if show: plt.show()
