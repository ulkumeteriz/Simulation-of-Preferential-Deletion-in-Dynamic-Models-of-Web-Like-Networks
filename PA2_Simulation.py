################
# Ulku Meteriz #
################

from decimal import *
from random import *

######################################################################################

def chooseBirth(nodes, totalDegrees):
  if len(nodes) == 1 or totalDegrees == 0:
    return nodes[0]
  r = randint(1, totalDegrees-1)
  for n in nodes:
    if r <= n.order:
      return n
    else:
      r -= n.order
  return nodes[len(nodes)-1]
      
def chooseDeath(nodes, denominator):
  
  if len(nodes) == 1 or denominator == 0:
    return nodes[0]
    
  r = randint(1, denominator-1)

  for n in nodes:
    if r <= len(nodes) - n.order:
      return n
    else:
      r -= (len(nodes) - n.order)
  return nodes[len(nodes)-1]
  
######################################################################################

class Node:
  def __init__(self):
    self.edges = []
    self.order = 0
  def addEdge(self, N):
    self.edges.append(N)
    self.order += 1

######################################################################################

class Graph:
  def __init__(self):
    self.nodes = []
    self.edges = []
    self.m = 0
    self.n = 0
  
  def addNode(self, N):
    self.nodes.append(N)
    self.n += 1
  
  def addEdge(self):
    self.m += 1
    
  def birth(self):

    # Choose the node that the new node will be attached.
    chosenNode = chooseBirth(self.nodes, 2 * self.m)
    
    # Create new node.
    N = Node()
    N.addEdge(chosenNode)
    
    # Attach new node to the chosen node.
    chosenNode.addEdge(N)
    
    # Add new node to the graph.
    self.addNode(N)
    
    # Add new edge to the graph.
    self.addEdge()
    
  def death(self):
    
    # Choose the node that will be deleted.
    nodeToBeDeleted = chooseDeath(self.nodes, pow(self.n,2) - 2 * self.m)
    
    # Go through the edges of chosen node and remove the edge from them.
    for n in nodeToBeDeleted.edges:
      n.edges.remove(nodeToBeDeleted)
    
    # Decrement number of edges in the graph.
    self.m -= nodeToBeDeleted.order
    
    # Decrement number of nodes in the graph.
    self.n -= 1
    
    # Remove the node from the graph.
    self.nodes.remove(nodeToBeDeleted)

######################################################################################

datasetN1 = []
datasetN2 = []
datasetN3 = []

datasetM1 = []
datasetM2 = []
datasetM3 = []

######################################################################################

# initial graph: a node with self loop.
N = Node()
N.addEdge(N)

G = Graph()
G.addNode(N)
G.addEdge()

# probability p = 0.6
# choose a random number in range [1,5], if it is smaller than 4, birth process
print "########## Probability p = 0.6 ##########"
t = 1
while t < 50000:
  
  if G.n == 0:
    print "GRAPH VANISHED STARTING OVER"
    t = 1
    N = Node()
    N.addEdge(N)
    G = Graph()
    G.addNode(N)
    G.addEdge()
  
  # sampling
  if t == 5000 or t == 15000 or t == 25000 or t == 35000 or t == 45000:
    print "t: " , t , "\tn: " , G.n, "\tm: " , G.m
    datasetN1.append(G.n)
    datasetM1.append(G.m)

  r = randint(1,5)

  if r < 4:
    G.birth()
  else:
    G.death()
  
  t += 1
 
####################################################################################### 
    
# initial graph: a node with self loop.
N = Node()
N.addEdge(N)

G = Graph()
G.addNode(N)
G.addEdge()

# probability p = 0.75
# choose a random number in range [1,4], if it is smaller than 3, birth process
print "########## Probability p = 0.75 ##########"
t = 1
while t < 50000:
  
  if G.n == 0:
    print "GRAPH VANISHED STARTING OVER"
    t = 1
    N = Node()
    N.addEdge(N)
    G = Graph()
    G.addNode(N)
    G.addEdge()
  
  # sampling
  if t == 5000 or t == 15000 or t == 25000 or t == 35000 or t == 45000:
    print "t: " , t , "\tn: " , G.n, "\tm: " , G.m
    datasetN2.append(G.n)
    datasetM2.append(G.m)
    
  r = randint(1,4)

  if r < 4:
    G.birth()
  else:
    G.death()
  
  t += 1
    
######################################################################################
    
# initial graph: a node with self loop.
N = Node()
N.addEdge(N)

G = Graph()
G.addNode(N)
G.addEdge()
    
# probability p = 0.9
# choose a random number in range [1,10], if it is smaller than 10, birth process
print "########## Probability p = 0.9 ##########"
t = 1
while t < 50000:
  
  if G.n == 0:
    print "GRAPH VANISHED STARTING OVER"
    t = 1
    N = Node()
    N.addEdge(N)
    G = Graph()
    G.addNode(N)
    G.addEdge()

  
  # sampling
  if t == 5000 or t == 15000 or t == 25000 or t == 35000 or t == 45000:
    print "t: " , t , "\tn: " , G.n, "\tm: " , G.m
    datasetN3.append(G.n)
    datasetM3.append(G.m)
    
  r = randint(1,10)

  if r < 10:
    G.birth()
  else:
    G.death()
    
  t += 1

#######################################################################################

# write the datasets to a file
f = open("results.txt", "w")
f.write(
    str(datasetN1) + "\n" +
    str(datasetN2) + "\n" +
    str(datasetN3) + "\n" +
    str(datasetM1) + "\n" +
    str(datasetM2) + "\n" +
    str(datasetM3) + "\n" )
f.close()

#######################################################################################

k = []
P_k = []
for n in G.nodes:
  if n.order not in k:
    k.append(n.order)
    P = Decimal(G.n - n.order) / Decimal(( pow(G.n,2) - 2 * G.m ))
    P_k.append(P) 
f = open("figure5.txt", "w")
f.write( str(k) + "\n" + str(P_k) )
f.close()

