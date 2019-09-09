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
        


matrix = Matrix()

for i in range(10):
    matrix.add_vertex()

print(matrix.return_items())