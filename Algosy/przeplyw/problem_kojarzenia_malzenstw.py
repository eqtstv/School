import collections
 
class Graph:

    def __init__(self, graph, colors):
        self.graph = graph
        self.ROW = len(graph)
        self.colors = colors
  
    def BFS(self, s, t):

        # Mark all the vertices as not visited
        visited = [False] * (self.ROW)
        parent = [None] * (self.ROW)
        
        # Create a queue for BFS
        queue = collections.deque()
        

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
        path = []
        
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
                    
                    if (ind == t):
                        path.append(ind)
                        
                        while (ind != s):
                            ind = parent[ind]
                            path.append(ind)
                        path.reverse()
                        
                        return path


    def pair(self):
        free = collections.deque()
        searching = collections.deque()
        paths = []
        matches = []
        counter = 0

        # add colored 1 as searching
        for v_index in range(len(self.colors)):
            if (self.colors[v_index] == 1):
                searching.append(v_index)

        # add colored 2 as free
        for v_index in range(len(self.colors)):
            if (self.colors[v_index] == 2):
                free.append(v_index)

        # loop over searching
        for v_searching in searching:
            # add empty path
            paths.append([])
            # loop over free
            for v_free in free:
                # BFS find shortest path between every searching x free
                path = self.BFS(v_searching, v_free)
                # append paths to all free for every searching
                paths[counter].append(path)

            # match searching to free by shortest path lenght
            match = (min(paths[counter], key=len))

            # remove matched v from free
            if (match[-1] in free):
                free.remove(match[-1])

            # if patch between searching - free == 2, add it
            if ((len(match) == 2)):
                matches.append(match)
            # else add it and cut it properly    
            else:
                # append match
                matches.append(match)
                # loop over patch lenght, step by 2
                for i in range(0, len(match), 2):
                    # match searching to first free, step by two
                    #  match i with i+1, then i+2 with i+3 ...
                    matches[match[i]] = [match[i], match[i+1]]
            counter += 1

        return matches


        

matrix = [
        # 0  1  2  3  4  5  6  7  8  9  
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0], #0
         [0, 0, 0, 0, 0, 1, 1, 0, 0, 0], #1
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], #2
         [0, 0, 0, 0, 0, 0, 1, 0, 1, 1], #3
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0], #4
         [0, 1, 1, 0, 0, 0, 0, 0, 0, 0], #5
         [0, 1, 0, 1, 0, 0, 0, 0, 0, 0], #6
         [1, 0, 0, 0, 1, 0, 0, 0, 0, 0], #7
         [1, 1, 0, 0, 1, 0, 0, 0, 0, 0], #8
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], #9
         ]

colors = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]

graph = Graph(matrix, colors)

print(graph.pair())
