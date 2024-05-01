%matplotlib inline
from ipywidgets import interactive
import matplotlib.pyplot as plt
import numpy as np
import math
import time
from IPython import display
print(" 1: graph and table of y= equation\n 2: Solve two equations without graph\n 3: Graph two equations and plot point of intersection\n 4: roots and vertex of quadratic equation")
choice = int(input("Select 1 through 4 "))

if choice == 1:
    def graph_table():
        equation = input("Enter y = equation: ")

        ax = plt.subplot()
        ax.set_axis_off()
        title = 'y=', equation
        cols = ('x', 'y')
        rows = [[0,0]]
        parts = equation.replace("x", "a")
        for a in range(1,10):
            rows.append([a, eval(parts)])

        ax.set_title(title)
        plt.table(cellText=rows, colLabels=cols, cellLoc='center', loc='upper left')
        plt.show()

        xmin = -20
        xmax = 20
        ymin = -20
        ymax = 20
        points = 2*(xmax-xmin)

        x = np.linspace(xmin,xmax,points)

        fig, ax = plt.subplots()
        plt.axis([xmin,xmax,ymin,ymax])
        plt.plot([xmin,xmax],[0,0],'b')
        plt.plot([0,0],[ymin,ymax], 'b')

        plt.plot(x, eval(equation))

    graph_table()

if choice == 2:
    def eq_gr():
        print("First equation: y = mx + b")
        mb_1 = input("Enter m and b, separated by a comma: ")
        mb_in1 = mb_1.split(",")
        m1 = float(mb_in1[0])
        b1 = float(mb_in1[1])

        print("Second equation: y = mx + b")
        mb_2 = input("Enter m and b, separated by a comma: ")
        mb_in2 = mb_2.split(",")
        m2 = float(mb_in2[0])
        b2 = float(mb_in2[1])

        x,y = symbols('x y')
        first = m1*x + b1 - y
        second = m2*x + b2 - y
        solution = linsolve([first, second], (x, y))
        x_solution = round(float(solution.args[0][0]),3)
        y_solution = round(float(solution.args[0][1]),3)

        print(" ")
        print("Solution: (", x_solution, ",", y_solution, ")")
    eq_gr()
if choice == 3:
    def eq_wo_gr():
        print("First equation: y = mx + b")
        mb_1 = input("Enter m and b, separated by a comma: ")
        mb_in1 = mb_1.split(",")
        m1 = float(mb_in1[0])
        b1 = float(mb_in1[1])

        print("Second equation: y = mx + b")
        mb_2 = input("Enter m and b, separated by a comma: ")
        mb_in2 = mb_2.split(",")
        m2 = float(mb_in2[0])
        b2 = float(mb_in2[1])

        x,y = symbols('x y')
        first = m1*x + b1 - y
        second = m2*x + b2 - y
        solution = linsolve([first, second], (x, y))
        x_solution = round(float(solution.args[0][0]),3)
        y_solution = round(float(solution.args[0][1]),3)

        xmin = int(x_solution) - 20
        xmax = int(x_solution) + 20
        ymin = int(y_solution) - 20
        ymax = int(y_solution) + 20
        points = 2*(xmax-xmin)

        graph_x = np.linspace(xmin,xmax,points)

        y1 = m1*graph_x + b1
        y2 = m2*graph_x + b2

        fig, ax = plt.subplots()
        plt.axis([xmin,xmax,ymin,ymax])
        plt.plot([xmin,xmax],[0,0],'b')
        plt.plot([0,0],[ymin,ymax], 'b')

        plt.plot(graph_x, y1)

        plt.plot(graph_x, y2)

        plt.plot([x_solution],[y_solution],'ro')

        plt.show()
        print(" ")
        print("Solution: (", x_solution, ",", y_solution, ")")
    eq_wo_gr()
if choice == 4:
    def rveq():
        print("y = ax\u00b2 + bx + c")

        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))

        vx = -b/(2*a)
        vy = a*vx**2 + b*vx + c



        print(" (", vx, " , ", vy, ")")
        print(" ")

        xmin = int(vx)-10
        xmax = int(vx)+10
        ymin = int(vy)-10
        ymax = int(vy)+10
        points = 2*(xmax-xmin)
        x = np.linspace(xmin,xmax,points)

        fig, ax = plt.subplots()
        plt.axis([xmin,xmax,ymin,ymax])
        plt.plot([xmin,xmax],[0,0],'b')
        plt.plot([0,0],[ymin,ymax], 'b')

        plt.plot([vx],[vy],'ro')

        x = np.linspace(vx-10,vx+10,100)
        y = a*x**2 + b*x + c
        plt.plot(x,y)

        plt.show()
    rveq()
