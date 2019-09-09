class Graph: 
	def __init__(self,vertices): 
		self.V= vertices
		self.graph = []
 
	def addEdge(self,u,v,w): 
		self.graph.append([u, v, w]) 
		 
	def printArr(self, dist): 
		print("Vertex | Distance from Source") 
		for i in range(self.V): 
			print("%d \t   |\t  %d" % (i, dist[i])) 
	
	def BellmanFord(self, src): 
        #set distances to all vertices to inf
		dist = [float("Inf")] * self.V
        #set source distance to 0
		dist[src] = 0

        #relax all edges v-1 times
		for i in range(self.V - 1): 
			for u, v, w in self.graph: 
				if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
						dist[v] = dist[u] + w 
        
        #check for negative weight cycles
		for u, v, w in self.graph: 
				if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
					print("Graph contains negative weight cycle")
					return
		# print all distances 
		self.printArr(dist) 



g = Graph(5) 
g.addEdge(0, 1, -1) 
g.addEdge(0, 2, 5) 
g.addEdge(1, 2, 5) 
g.addEdge(1, 3, 7) 
g.addEdge(1, 4, 10)
g.addEdge(3, 2, 3) 
g.addEdge(3, 1, 6) 
g.addEdge(4, 3, -2) 

g.BellmanFord(0) 