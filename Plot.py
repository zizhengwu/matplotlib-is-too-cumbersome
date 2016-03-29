import matplotlib.pyplot as plt
from matplotlib import lines
from itertools import cycle


class Plot:
    def __init__(self, **arg):
        fig1 = plt.figure()
        styles = lines.lineStyles.keys()
        linecycler = cycle(styles)
        for data in arg['data']:
            plt.plot(data['x'], data['y'], next(linecycler), label=data['label'])
        plt.xlabel(arg['xlabel'])
        plt.ylabel(arg['ylabel'])
        plt.show()