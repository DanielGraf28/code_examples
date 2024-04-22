%matplotlib inline
from ipywidgets import interactive
import matplotlib.pyplot as plt
import numpy as np
import math
import time
from IPython import display

import random
print("choose a game.\n1: Scatter plot game\n2: Algebra practice game\n3: Projectile game")
choice = int(input("Select 1 - 3 "))
if choice == 1:
  def scatter():
    score = 0

    xmin = -30
    xmax = 30
    ymin = -30
    ymax = 30

    fig, ax = plt.subplots()

    for i in range(0,3):
      xpoint = random.randint(xmin, xmax)
      ypoint = random.randint(ymin, ymax)
      x = [xpoint]
      y = [ypoint]
      plt.axis([xmin,xmax,ymin,ymax])
      plt.plot([xmin,xmax],[0,0],'b')
      plt.plot([0,0],[ymin,ymax], 'b')
      plt.plot(x, y, 'ro')
      print(" ")
      plt.grid()
      plt.show()
      guess = input("Enter the coordinates of the red point point: \n")
      guess_array = guess.split(",")
      xguess = int(guess_array[0])
      yguess = int(guess_array[1])
      if xguess == xpoint and yguess == ypoint:
        score = score + 1

    print("Turns left ", score)
  scatter()
if choice == 2:
  def apg():
    def string_frac(in_string):
      if "/" in in_string:
        nd = in_string.split("/")
        n = float(nd[0])
        d = float(nd[1])
        ans = n/d
        return ans
      else:
        ans = float(in_string)
        return ans


    def one_step_add():
      import random
      a = random.randint(-4,10)
      b = random.randint(2,24)
      print("x + ", a, " = ", b)
      ans = float(input("x = "))
      answer = b-a
      if ans==answer:
        print("Correct! \n")
      else:
        print("Try again")
        print("The correct answer is ", answer, "\n")


    def one_step_subtract():
      import random
      a = random.randint(-19,-1)
      b = random.randint(2,24)
      print(a, " + x = ", b)
      ans = float(input("x = "))
      answer = b-a
      if ans==answer:
        print("Correct! \n")
      else:
        print("Try again")
        print("The correct answer is ", answer, "\n")

    def one_step_mult():
      import random
      a = random.randint(1,11)
      b = random.randint(2,24)
      print(a, "x = ", b)
      print("Round your answer to two decimal places.")
      ans_in = (input("x = "))
      answer = round(b/a,2)
      if string_frac(ans_in)==answer:
        print("Correct! \n")
      else:
        print("Try again")
        print("The correct answer is ", answer, "\n")


    def one_step_div():
      import random
      a = random.randint(1,11)
      b = random.randint(2,24)
      print("x/", a, " = ", b)
      ans = float(input("x = "))
      answer = b*a
      if ans==answer:
        print("Correct! \n")
      else:
        print("Try again")
        print("The correct answer is ", answer, "\n")


    def two_step():
      import random
      a = random.randint(1,11)
      b = random.randint(-7,12)
      c = random.randint(2,36)
      print(a, "x + ", b, " = ", c)
      print("Round answer to two decimal places")
      ans_in = input("x = ")
      answer = (c-b)/a

      if round(string_frac(ans_in),2)==round(answer,2):
        print("Correct! \n")
      else:
        print("Try again")
        print("The correct answer is ", answer, "\n")


    for a in range(2):
      one_step_add()
      one_step_subtract()
      one_step_mult()
      one_step_div()
      two_step()
      print(" ")

    two_step()
    two_step()
  scatter()
if choice == 3:
  def projectile():
    def f(b):
      d = random.randint(1, 100)
      f = random.randint(1,5000)
      plt.axis([0,100,0,10000])
      plt.plot([-10,10],[0,0],'k')
      plt.plot([0,0],[-10,10], 'k')
      x = np.linspace(-400, 400, 1000)
      plt.plot([d,d],[0,f],'r')
      plt.plot(x, -4.9*x**2 + b*x + 0)
      plt.show()

    interactive_plot = interactive(f,b=(0,500))
    interactive_plot
  projectile()
else:
  print("Invalid Entry")



def f(b):
    d = random.randint(1, 100)
    f = random.randint(1,5000)
    plt.axis([0,100,0,10000])
    plt.plot([-10,10],[0,0],'k')
    plt.plot([0,0],[-10,10], 'k')
    x = np.linspace(-400, 400, 1000)
    plt.plot([d,d],[0,f],'r')
    plt.plot(x, -4.9*x**2 + b*x + 0)
    plt.show()

interactive_plot = interactive(f,b=(0,500))
interactive_plot
