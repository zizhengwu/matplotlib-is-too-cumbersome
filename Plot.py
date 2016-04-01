import matplotlib.pyplot as plt
from matplotlib import lines
from itertools import cycle


class Plot:
    def __init__(self, **arg):
        fig1 = plt.figure()
        dot_styles = ['b--', 'gs', 'r^', 'cp', 'm*'].__iter__()
        line_styles = ['b-', 'g-', 'r-', 'c-', 'm-'].__iter__()
        for data in arg['data']['dots']:
            plt.plot(data['x'], data['y'], next(dot_styles), label='Bloom filter table size = ' + str(data['label']))
        for data in arg['data']['lines']:
            plt.plot(data['x'], data['y'], next(line_styles), label='Bloom filter table size = ' + str(data['label'] + ' theoretical'))
        axes = plt.gca()
        if 'xlimit' in arg:
            axes.set_xlim(arg['xlimit'])
        if 'ylimit' in arg:
            axes.set_ylim(arg['ylimit'])
        plt.xlabel(arg['xlabel'])
        plt.ylabel(arg['ylabel'])
        plt.legend(loc=4)
        plt.show()