import matplotlib.pyplot as plt

def discret_plot(x, y, width = 12, marker = 'go', show = True, save_path = None, title = None, x_label = None, y_label = None, font_size_label = 10) -> None:
    plt.clf()
    plt.grid(True)
    figure = plt.figure(1)
    figure.set_figwidth(width)
    plt.stem(x, y, markerfmt=marker)
    plt.title(title)
    plt.ylabel(y_label, fontsize = font_size_label)
    plt.xlabel(x_label, fontsize = font_size_label)
    if save_path != None:
        plt.savefig(save_path)
    if show:
        plt.show()
