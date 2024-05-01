import pandas as pd
import matplotlib.pyplot as plt
from google.colab import files
import io
import numpy

print("Get data from\n1: Computer\n2: url")
choice = int(input("Enter 1 or 2 "))
if choice == 1:
  document = input("Enter file name")
  uploaded = files.upload(document)
  file_name = next(iter(uploaded))
  table = pd.read_csv(io.BytesIO(uploaded[file_name]))
  print(table.head(2))
  cols = table.columns
  print("columns")
  for a in range(len(cols)):
    print(a, " ", cols[a] )
  print("Enter which column to graph")
  choice_2 = int(input("Enter column number "))
  new_col = cols[choice_2]
  y = table[cols[choice_2]].to_numpy()
  x = table[cols[0]].to_numpy()
  xmin = x.min() - 5
  xmax = x.max() + 5
  ymin = y.min() - 5
  ymax = y.max() + 5

  fig, ax = plt.subplots()
  plt.axis([xmin,xmax,ymin,ymax])
  plt.plot([xmin,xmax],[0,0],'b')
  plt.plot([0,0],[ymin,ymax],'b')
  plt.plot(x,y,'ro')
  ax.set_xlabel(cols[0])
  ax.set_ylabel(new_col)
  plt.show()
if choice == 2:
  url = input("Enter url ")
  table = pd.read_csv(url)
  print(table.head(2))
  cols = table.columns
  print("columns")
  for a in range(len(cols)):
    print(a, " ", cols[a] )
  print("Enter which column to graph")
  choice_2 = int(input("Enter column number "))
  new_col = cols[choice_2]
  y = table[cols[choice_2]].to_numpy()
  x = table[cols[0]].to_numpy()
  xmin = x.min() - 5
  xmax = x.max() + 5
  ymin = y.min() - 5
  ymax = y.max() + 5

  fig, ax = plt.subplots()
  plt.axis([xmin,xmax,ymin,ymax])
  plt.plot([xmin,xmax],[0,0],'b')
  plt.plot([0,0],[ymin,ymax],'b')
  plt.plot(x,y,'ro')
  ax.set_xlabel(cols[0])
  ax.set_ylabel(new_col)
  plt.show()
else:
  print("Invalid Entry")
