################
# Ulku Meteriz #
################

import matplotlib.pyplot as plt
from decimal import *

def stringToList(string):
  string = string.replace("[","")
  string = string.replace("]","")
  string = string.replace(",","")
  L = string.split(' ')
  i = 0
  while i < len(L):
    L[i] = int(L[i])
    i += 1
  return L

def convert(string):
  string = string.replace("[","")
  string = string.replace("]","")
  string = string.replace(")","")
  string = string.replace(",","")
  string = string.replace("Decimal('", "")
  string = string.replace("'", "")
  L = string.split(' ')
  i = 0
  while i < len(L):
    L[i] = Decimal(L[i])
    i += 1
  return L

def drawLineGraph(y06, y075, y09, yLabel, title):
  # x axis values 
  x = [1,5000,15000,25000,35000,45000] 
  
  # setting x axis range 
  plt.xlim(0,50000)
  
  # plotting the points  
  plt.plot(x, y06, color='green', linestyle='-', linewidth = 3, 
           marker='o', markerfacecolor='blue', markersize=12, label='p = 0.6')

  plt.plot(x, y075, color='green', linestyle='-', linewidth = 3, 
           marker='v', markerfacecolor='red', markersize=12, label='p = 0.75')
  
  plt.plot(x, y09, color='green', linestyle='-', linewidth = 3, 
           marker='D', markerfacecolor='yellow', markersize=12, label='p = 0.9')
  
  plt.legend(loc=2)
  
  plt.xlabel('t') 
  plt.ylabel(yLabel) 
  plt.title(title) 
  plt.show()

###############################################################
f = open("results.txt", "r")

nodeP06 = [1] + stringToList(f.readline())
nodeP075 = [1] + stringToList(f.readline())
nodeP09 = [1] + stringToList(f.readline())
edgeP06 = [1] + stringToList(f.readline())
edgeP075 = [1] + stringToList(f.readline())
edgeP09 = [1] + stringToList(f.readline())

drawLineGraph(nodeP06, nodeP075, nodeP09, "Number of Nodes", "")

drawLineGraph(edgeP06, edgeP075, edgeP09, "Number of Edges", "")

f.close()
###############################################################

f = open("figure5.txt", "r")

# get the orders
x = stringToList(f.readline())
# get the probabilities
y = convert(f.readline())

# plotting the points  
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, 
         marker='o', markerfacecolor='blue', markersize=12) 
plt.xlabel('k') 
plt.ylabel('P\'(k)') 
plt.title("Cumulative Degree Distribution of the Graph") 
plt.show()

f.close()

