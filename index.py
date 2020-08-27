from pandas import read_csv as rc;from random import randint as ri
import statistics as sts;import plotly.figure_factory as ff
p = "data.csv"
def rx(x, y):
    return sts.mean([y[ri(0, len(y)-1)] for i in range(x)])
x = [rx(30, rc(p)['temp']) for i in range(100)]
print("Mean of population: {}\nMean of sample: {}".format(sts.mean(rc(p)["temp"]), sts.mean(x)))
ff.create_distplot([x], [""], show_hist=False).show()
