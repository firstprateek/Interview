# DISJOINT SET

# UNION BY SIZE

class DisjointSet:
  def __init__(self, objects):
    size = len(objects)
    self.ids = list(range(size))
    self.map = { val: i for i, val in enumerate(objects) }
    self.sizes = [1] * size
    self.number_of_components = size

  def union(self, obj1, obj2):
    obj1_id = self.find(obj1)
    obj2_id = self.find(obj2)

    if obj1_id == obj2_id:
      return False

    if self.sizes[obj1_id] >= self.sizes[obj2_id]:
      self.ids[obj2_id] = obj1_id
      self.sizes[obj1_id] += self.sizes[obj2_id]
      self.sizes[obj2_id] = 0
    else:
      self.ids[obj1_id] = obj2_id
      self.sizes[obj2_id] += self.sizes[obj1_id]
      self.sizes[obj1_id] = 0

    self.number_of_components -= 1

    return True

  def find(self, obj):
    obj_id = self.map[obj]
    orig_id = obj_id

    while obj_id != self.ids[obj_id]:
      obj_id = self.ids[obj_id]

    #path compression
    while orig_id != obj_id:
      parent_id = self.ids[orig_id]
      self.ids[orig_id] = obj_id
      orig_id = parent_id

    return obj_id

# KRUSKAL
class Kruskal:
  def __init__(self, edges):
    self.edges = sorted(edges, key=lambda x: x[2])
    self.vertex = set()
    
    for a, b, dist in edges:
      self.vertex.add(a)
      self.vertex.add(b)

  def findMST(self):
    d_set = DisjointSet(self.vertex)
    mst = []

    for edge in self.edges:
      a, b, dist = edge
      if not d_set.union(a, b):
        continue

      mst.append(edge)

    return mst

inputs = [
  [["Acity","Bcity",1], ["Acity","Ccity",2], ["Bcity","Ccity",3]],
  [["Acity","Bcity",2], ["Bcity","Dcity",5], ["Acity","Dcity",4], ["Ccity","Ecity",1]]
]

for inp in inputs:
  kruskal = Kruskal(inp)
  print(kruskal.findMST())

# FIND CYCLE IN UNDIRECTED GRAPH

