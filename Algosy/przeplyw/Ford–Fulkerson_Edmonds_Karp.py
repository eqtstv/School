import collections
 
class Graph:

    def __init__(self,graph):
        self.graph = graph
        self.ROW = len(graph)
  
    def BFS(self, s, t, parent):

        # Mark all the vertices as not visited
        visited = [False] * (self.ROW)
        
        # Create a queue for BFS
        queue = collections.deque()

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        # Standard BFS Loop
        while queue:
            u = queue.popleft()
         
            # Get all adjacent vertices's of the dequeued vertex u
            # If an adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if (visited[ind] == False) and (val > 0):
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
 
        # If we reached sink in BFS starting from source, then return
        # true, else false
        return visited[t]

    def EdmondsKarp(self, source, sink):
 
        # This array is filled by BFS and to store path
        parent = [0] * (self.ROW)

        # Starting flow is 0
        max_flow = 0
 
        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent):
 
            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
 
            # Add path flow to overall flow
            max_flow += path_flow
 
            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while v !=  source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
 
        return max_flow

         # 0, 1, 2, 3, 4, 5
matrix = [[0, 16, 13, 0, 0, 0],
         [0, 0, 10, 12, 0, 0],
         [0, 4, 0, 0, 14, 0],
         [0, 0, 9, 0, 0, 20],
         [0, 0, 0, 7, 0, 4],
         [0, 0, 0, 0, 0, 0]]


graph = Graph(matrix)

max_flow = graph.EdmondsKarp(0, 5)

print('Maximal flow: ' + str(max_flow))