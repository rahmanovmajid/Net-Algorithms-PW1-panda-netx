import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib import style
style.use('ggplot')
plt.rcParams['figure.figsize'] = [16,12]
plt.rcParams.update({'font.size':18})

data = pd.read_csv('cities_in_az.csv')

Graph = nx.from_pandas_edgelist(data, source='Origin', target='Destiny', edge_attr=True)

plt.figure()
nx.draw_networkx(Graph, with_labels=True) 
plt.show()

def track(Graph,start, stop):
  path = [start] 
  for elem in list(Graph.neighbors(start)):
    # if (start == stop):
    #   return start
    if (stop == elem):
      path.append(elem)
      return path
    else: 
      path += track(Graph,elem, stop)
      return path

def calc_hours(Graph,origin, destination):
  sum = 0
  path = track(Graph,origin, destination)
  for i in range(len(path)-1):
    node1,node2 = path[i],path[i + 1]
    sum+=Graph.edges[node1, node2]['Hours']
  return sum


print(calc_hours(Graph,'Kurdamir', 'Baku'))
print(track(Graph,'Kurdamir', 'Baku'))

