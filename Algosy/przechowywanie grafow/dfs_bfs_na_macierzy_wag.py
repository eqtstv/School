import numpy as np

class Matrix:
    def __init__(self):
        self.items = np.array([], dtype=int)

    def return_items(self):
        return self.items
        
    def shape(self):
        return self.items.shape[0]

    def add_vertex(self):
        #dodaj pierwszy wierzchołek
        if (self.items.shape[0] == 0):
            self.items = np.append(self.items, [0])
        #dodawanie kolejnych wierzchołków
        else:
            #dodaj nowy wiersz do macierzy [n+1 x n]
            self.items = np.vstack((self.items, np.zeros(self.items.shape[0])))
            #dodaj nową kolumnę do macierzy [n+1 x n+1]
            self.items = np.column_stack((self.items, np.zeros(self.items.shape[0])))

    def delete_vertex(self, v_index):
        #sprawdź czy istnieje taki wierzchołek
        if (self.items.shape[0] >= v_index > 0):
            #usuń wiersz
            self.items = np.delete(self.items, v_index - 1, 0)
            #usuń kolumnę
            self.items = np.delete(self.items, v_index - 1, 1)
        else:
            print('Nie ma takiego wierzcholka')

    def add_edge(self, v_out, v_in, weight):
        #sprawdź czy podane wierzcołki instnieją, i czy wprowadzane v_in i v_out nie są 0
        if (self.items.shape[0] >= v_out > 0  and self.items.shape[0] >= v_in > 0):
            #zmień wagę krawędzi
            self.items[v_out - 1][v_in - 1] = weight
        else:
            print('Zle wprowadzony wierzcholek wejsciowy, lub wyjsciowy')

    def delete_edge(self, v_out, v_in):
        #sprawdź czy podane wierzcołki instnieją, i czy wprowadzane v_in i v_out nie są 0
        if (self.items.shape[0] >= v_out > 0  and self.items.shape[0] >= v_in > 0):
            #ustaw wagę krawędzi na 0
            self.items[v_out - 1][v_in - 1] = 0
        else:
            print('Zle wprowadzony wierzcholek wejsciowy, lub wyjsciowy')
        

def dfs(graph, init_v):
    stack = []
    discovered = []
    stack.append(init_v)

    while stack:
        v = stack.pop()
        print('wierzcholek')
        print(v + 1)
        if v not in discovered:
            discovered.append(v)
            print('discovered')
            print(discovered)
            row = graph[v]
            print('row')
            print(row)
            for i in range(len(row)):
                if row[i] != 0:
                    stack.append(i)
                    print('odkryte')
                    print(i + 1)
                    print('\n')
    return discovered

def bfs(graph, init_v):
    queue = []
    discovered = []
    queue.insert(0, init_v)

    while queue:
        v = queue.pop()
        print('wierzcholek')
        print(v + 1)
        if v not in discovered:
            discovered.append(v)
            print('discovered')
            print(discovered)
            row = graph[v]
            print('row')
            print(row)
            for i in range(len(row)):
                if row[i] != 0:
                    queue.append(i)
                    print('odkryte')
                    print(i + 1)
                    print('\n')
    return discovered


matrix = Matrix()

for i in range(4):
    matrix.add_vertex()

matrix.add_edge(1, 2, 1)
matrix.add_edge(1, 4, 1)
matrix.add_edge(2, 1, 1)
matrix.add_edge(2, 3, 1)
matrix.add_edge(2, 4, 1)
matrix.add_edge(3, 1, 1)
matrix.add_edge(3, 4, 1)
matrix.add_edge(4, 4, 1)


print(matrix.return_items())
print('\n')

graph = matrix.return_items()


print(bfs(graph, 0))

print('\n -----------------------------')

print(dfs(graph, 0))