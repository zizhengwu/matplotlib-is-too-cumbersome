from Plot import Plot
import numpy


if __name__ == '__main__':
    data = {}
    for filename in ['256.txt', '512.txt', '1024.txt', '2048.txt', '4096.txt']:
        int_name = int(filename.split('.')[0])
        data[int_name] = {}
        data[int_name]['x'] = []
        data[int_name]['y'] = []
        with open('data/' + str(filename), 'r') as lines:
            for line in lines:
                data[int_name]['x'].append(int(line.split('\t')[0].strip()))
                data[int_name]['y'].append(float(line.split('\t')[1].strip()))

    to_be_ploted_dots = []
    for k, v in sorted(data.items()):
        to_be_ploted_dots.append({'x': v['x'], 'y': v['y'], 'label': k})

    x = numpy.linspace(1, 4000, 4000)
    y = [numpy.exp(numpy.log(2)*numpy.log(2)*-(256/x)), numpy.exp(numpy.log(2)*numpy.log(2)*-(512/x)), numpy.exp(numpy.log(2)*numpy.log(2)*-(1024/x)), numpy.exp(numpy.log(2)*numpy.log(2)*-(2048/x)), numpy.exp(numpy.log(2)*numpy.log(2)*-(4096/x))]
    to_be_ploted_lines = []
    label = ['256', '512', '1024', '2048', '4096'].__iter__()
    for v in y:
        to_be_ploted_lines.append({'x': x, 'y': v, 'label': next(label)})
    plot = Plot(data={'dots': to_be_ploted_dots, 'lines': to_be_ploted_lines}, xlabel='# of items added into the subset that our Bloom filter is maintaining', ylabel='false positive probability', xlimit=[0, 4000])
