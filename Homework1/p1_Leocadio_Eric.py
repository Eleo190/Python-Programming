#Problem 1: Quadratic Equations
import math
import numpy as np
import matplotlib.pyplot as plt

a = "blank"
while a != "":
    #Take in all inputs as strings to check if a is blank, if not make a,b,c floats
    a = input("Enter coefficient a: ")
    if a == "": break
    b = input("Enter coefficient b: ")
    c = input("Enter coefficient c: ")
    a, b, c = float(a), float(b), float(c)

    discriminant = (b**2) - (4*a*c)
    if discriminant < 0:
        print("no real solutions")
        #Finds max or min value of the equation to center graph on
        center_value = -b / (2*a)
        domain_max = center_value + 5
        domain_min = center_value - 5
    elif discriminant == 0:
        x1 = (-b + math.sqrt(discriminant))/(2*a)
        print(f"one solution: {x1}")
        #Centers graph on single root
        domain_max = x1 + 5
        domain_min = x1 - 5
    elif discriminant > 0:
        x1 = (-b - math.sqrt(discriminant))/(2*a)
        x2 = (-b + math.sqrt(discriminant))/(2*a)
        print(f"two solutions: x1={x1}, x2={x2}")
        #Graph is spaced evenly past each root
        domain_max = max(x1, x2) + 5
        domain_min = min(x1, x2) - 5

    #Making linspace for graph to be made
    x = np.linspace(domain_min, domain_max, 150)
    y = a*(x**2) + (b*x) + c

    #Make table
    plt.figure()
    plt.plot(x, y)
    plt.grid(True)
    plt.title("Quadratic Function Graph")
    plt.show()

    