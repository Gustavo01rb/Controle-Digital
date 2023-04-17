import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

def plot(
        data            : list, 
        range           : list   = [], 
        width           : float  = 12  , 
        marker          : str    = 'go', 
        show            : bool   = True, 
        save_path       : str    = None, 
        title           : str    = '', 
        x_label         : str    = '', 
        y_label         : str    = '', 
        font_size_label : int    = 10,
        discret         : bool   = True ,
        grid            : bool   = True,
        multiline       : bool   = False,
        overlapping     : bool   = False,
        ) -> None:
    
    plt.clf()
    plt.grid(grid)

    if not multiline:
        figure = plt.figure(1)
        figure.tight_layout()
        figure.set_figwidth(width)
        plt.stem(range, data, markerfmt=marker) if discret else plt.plot(range,data, marker) 
        plt.title(title)
        plt.ylabel(y_label, fontsize = font_size_label)
        plt.xlabel(x_label, fontsize = font_size_label)
    else:
        fig, axs = plt.subplots(len(data) if not overlapping else len(data) +1)
        fig.tight_layout()
        fig.subplots_adjust(top=0.9, right=0.85)
        fig.set_figwidth(21)
        fig.set_figheight(12)

        if title:  fig.suptitle(title,fontsize=22, fontweight ="bold")
        last = len(data)
        for index, function in enumerate(data):
            if not discret in function and  function['discret']:
                axs[index].stem(function['range'], function['data'], markerfmt=function['marker'] if 'marker' in function else marker)
                if overlapping: axs[last].stem(
                        function['range'], function['data'], 
                        markerfmt = function['marker'] if 'marker' in function else marker , 
                        label = function['label'] if 'label' in function else None
                    )
            else:
                axs[index].plot(function['range'], function['data'])
                if overlapping: axs[last].plot(function['range'], function['data'], label = function['label'] if 'label' in function else None)

            if index == last - 1:
                if overlapping:
                    axs[last].legend(loc='center left', bbox_to_anchor=(1, 0.5),prop={'size': 20})

            if 'title' in function: 
                axs[index].set_title(function['title'], loc='left',fontsize=16, fontweight =200)
    
    if save_path != None:
        plt.savefig(save_path)
    if show:
        plt.show()


def pzplot(p,z) -> None:
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
    plt.show()