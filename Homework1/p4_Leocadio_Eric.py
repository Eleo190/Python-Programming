#Problem 4: Function visualization
import math
import matplotlib.pyplot as plt

def plot_function(fun_str, domain, ns):
    #divide length of domain by amount of gaps to find equal step length
    step = ((max(domain)-min(domain)) / (ns-1))
    xs = []
    for x in range (ns):
        xs.append(min(domain) + x*step) 
    ys = []
    for x in xs:
        y = eval(fun_str)
        ys.append(y)
    print("\tx\ty")
    print("_"*30)
    for val in range (ns):
        print("\t{:.4f}\t{:.4f}".format(xs[val], ys[val]))
    plt.figure()
    plt.plot(xs, ys)
    plt.grid(True)
    plt.title(fun_str)
    plt.show()

#Take in all the params
fun_str = input("Enter the function here: ")
domain = []
ns = int(input("Enter the amount of samples: "))
domain.append(float(input("Enter xmin: ")))
domain.append(float(input("Enter xmax: ")))
domain = tuple(domain)
plot_function(fun_str, domain, ns)