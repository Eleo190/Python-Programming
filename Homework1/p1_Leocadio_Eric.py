#Problem 1: Quadratic Equations
import math
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

    #Making graph variables
    steps = (domain_max-domain_min)/149
    xs = []
    ys = []
    for i in range (0,150): xs.append(domain_min + (i*steps))
    for x in xs:
        ys.append(a*(x**2) + (b*x) + c)

    #Make table
    plt.figure()
    plt.plot(xs, ys)
    plt.grid(True)
    plt.title("Quadratic Function Graph")
    plt.show()

    