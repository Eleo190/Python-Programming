#Problem 4: Function visualization
import math
import matplotlib.pyplot as plt

def plot_function(fun_str, domain, ns):
    step = ((max(domain)-min(domain)) / ns-1)
    xs = []
    for x in range (ns):
        xs.append(min(domain) + x*step) 
    ys = []
    for x in xs:
        y = eval(fun_str)
        ys.append(y)
    print("\tx\ty\n____________")
    for val in range (150):
        print("\t{}\t{}".format(xs(val), ys(val)))

