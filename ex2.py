import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib import style
style.use('ggplot')
plt.rcParams['figure.figsize'] = [16,12]
plt.rcParams.update({'font.size':18})


data = pd.read_csv('airports.csv')
Graph = nx.from_pandas_edgelist(data, source='Origin', target='Dest', edge_attr=True)

def attribute_for_nodes(G, attribute, default_value):
    for g in G.nodes.keys():
        G.nodes[g][attribute] = default_value
attribute_for_nodes(Graph, 'time', 0)

plt.figure()
nx.draw_networkx(Graph, with_labels=True) 
plt.show()

def track(Graph,start, destination):
  path = [start] 
  for i in list(Graph.neighbors(start)):
    # if (start == destination):
    #   return start
    if (destination == i):
      path.append(i)
      return path
    else: 
      path = path + track(Graph,i, destination)
      return path

def distance(Graph,start,stop):
  dist = 0
  path = track(Graph,start, stop)
  for i in range(len(path)-1):
    node1,node2 = path[i],path[i + 1]
    dist+= Graph.edges[node1, node2]['Distance']
  return dist

def airtime(Graph,start, stop):
  duration = 0
  path = track(Graph,start, stop)
  for i in range(0,len(path)-1):
    node1,node2 = path[i],path[i + 1]
    duration += Graph.edges[node1, node2]['AirTime']
  return duration
