%matplotlib inline
from ipywidgets import interactive
import matplotlib.pyplot as plt
import numpy as np
import math

print("1: Mortgage payments\n2: Retirement calculator\n3: Time to double money\n4: Rate of growth")
c = int(input("select 1 through 4"))
if c == 1:
  def mortgage():
    p = float(input("Amount borrowed: "))
    r = float(input("Annual percentage rate: "))
    t = float(input("Number of years: "))

    mult = 1+r/12
    exp = 12*t
    top = r/12*mult**exp
    bot = (mult**exp)-1
    pmt = p*(top/bot)


    print("Monthly payment = $", pmt)
  mortgage()

  def investments():

    p = float(input("Starting amount: "))
    r = float(input("Annual percentage rate: "))
    t = int(input("Number of years: "))
    monthly = float(input("Monthly contribution: "))

    annuity = p

    for a in range(12*t):
      annuity = annuity + monthly
      interest = annuity * r / 12
      annuity = annuity + interest

    print("Annuity = ", annuity)
  investments()
if c == 2:
  p = float(input("Starting amount: "))
  r = float(input("Annual percentage rate: "))
  t = int(input("Number of years: "))
  monthly = float(input("Monthly contribution: "))

  annuity = p

  for a in range(12*t):
    annuity = annuity + monthly
    interest = annuity * r / 12
    annuity = annuity + interest

  print("Annuity = ", annuity)
if c == 3:
  p = float(input("Starting amount: "))
  r = float(input("Percentage rate, converted to a decimal: "))
  n = int(input("Number of times compounded per year: "))

  t = math.log(2)/(n*math.log(1+(r/n)))
  print(t)
if c == 4:
  p = float(input("Principle: "))
  t = int(input("Time: "))
  n = int(input("N: "))
  a = float(input("end amount: "))

  r = n*((a/p)**(1/(n*t))-1)

  print(r)
